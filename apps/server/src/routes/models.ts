import z from "zod";
import { protectedProcedure } from "../trpc";
import { ModelState } from "@prisma/client";

export const modelsRoute = protectedProcedure
  .query(async ({ ctx }) => {
    return ctx.db.models.findMany({
      where: {
        userId: ctx.user?.sub,
      },
      orderBy: {
        createdAt: "desc",
      },
    });
  });
