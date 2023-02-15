import type { Media, CreateMedia, UpdateMedia } from "@/interfaces/Media.js";
import createCRUDroutes from "@/networking/crud.base";

const crudRoutes = createCRUDroutes(
  new Object() as CreateMedia,
  new Object() as Media,
  new Object() as UpdateMedia,
  "media"
);

export default {
  create: crudRoutes.create,
  list: crudRoutes.list,
  read: crudRoutes.read,
  update: crudRoutes.update,
  delete: crudRoutes.delete,
};
