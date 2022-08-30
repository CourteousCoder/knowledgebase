const { google } = require("googleapis");
const GoogleOAuth2 = require("google-oauth2-env-vars");
const { ENV_TOKEN_VAR } = require("./constants");
const { GoogleDocument } = require("./google-document");
const {
  writeDocumentToTests,
} = require("../../gdocs2md/src/write-document-to-tests");
const { fetchFiles } = require("./google-drive");

async function fetchDocument(id) {
  const googleOAuth2 = new GoogleOAuth2({
    token: ENV_TOKEN_VAR,
  });
  const auth = await googleOAuth2.getAuth();

  const res = await google.docs({ version: "v1", auth }).documents.get({
    documentId: id,
  });

  if (!res.data) {
    throw new Error("Empty Data");
  }

  return res.data;
}

/** @param {import('../..').Options} options */
async function fetchDocuments(options) {
  const documentsProperties = await fetchFiles(options);
  const links = documentsProperties.reduce(
    (acc, properties) => ({ ...acc, [properties.id]: properties.slug }),
    {}
  );

  const googleDocuments = await Promise.all(
    documentsProperties.map(async (properties) => {
      const document = await fetchDocument(properties.id);
      const googleDocument = new GoogleDocument({
        document,
        properties,
        options,
        links,
      });
      return googleDocument;
    })
  );

  return googleDocuments;
}

module.exports = {
  fetchDocuments,
};
