import path from "path";
import { jekyllifyDocs } from "../src/jekyllUtils.js";
import { config } from "dotenv";
// Read .env file from directory where command is issued
config({ path: path.resolve(process.cwd(), ".env") });
const folderId = process.env.TEST_GDRIVE_ROOT_ID;
const root = process.env.TEST_LOCAL_ROOT_DIR;
const suffix = process.env.TEST_SUFFIX;
const pluginOptions = {
  folder: folderId,
  targetMarkdownDir: path.join(
    root,
    "actual-results/markdowns-generated-from-google-drive"
  ),
  suffix: suffix,
  extension: "md",
  saveGdoc: false,
  saveMarkdown: true,
};

jekyllifyDocs(pluginOptions);