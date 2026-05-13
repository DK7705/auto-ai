import express from "express";
import * as trpcExpress from "@trpc/server/adapters/express";
import { createContext, t } from "./src/trpc";
import { statsRoute } from "./src/routes/stats";
import cors from "cors";
import { modelsRoute } from "./src/routes/models";
import { uploadRoute } from "./src/routes/upload";
import { trainRoute } from "./src/routes/train";
import { inferenceRoute, inferenceHistoryRoute, getInferenceRoute } from "./src/routes/inference";

const app = express();

const PORT = process.env.PORT || 3000;

const appRouter = t.router({
  stats: statsRoute,
  models: modelsRoute,
  upload: uploadRoute,
  train: trainRoute,
  inference: inferenceRoute,
  inferenceHistory: inferenceHistoryRoute,
  getInference: getInferenceRoute,
});

app.use(
  cors({
    origin: "*",
    credentials: true,
  })
);

app.use(
  "/trpc",
  trpcExpress.createExpressMiddleware({
    router: appRouter,
    createContext,
  })
);

app.use("/trpc-panel", async (_, res) => {
  try {
    const { renderTrpcPanel } = await import("trpc-ui");
    return res.send(renderTrpcPanel(appRouter, { url: "/trpc" }));
  } catch (error) {
    return res.status(500).send("tRPC Panel is unavailable (Zod v4 compatibility issue with trpc-ui). Use the tRPC endpoints directly.");
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on port http://localhost:${PORT}`);
});
export type AppRouter = typeof appRouter;
