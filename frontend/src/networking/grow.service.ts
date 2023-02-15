import type { CreateGrow, Grow, UpdateGrow } from "@/interfaces/Grow.js";
import createCRUDroutes from "@/networking/crud.base";

const crudRoutes = createCRUDroutes(
  new Object() as CreateGrow,
  new Object() as Grow,
  new Object() as UpdateGrow,
  "grows"
);

export default {
  list: crudRoutes.list,
  create: crudRoutes.create,
  read: crudRoutes.read,
  update: crudRoutes.update,
  delete: crudRoutes.delete,
};
