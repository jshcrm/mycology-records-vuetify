import type { Spawn, CreateSpawn, UpdateSpawn } from "@/interfaces/Spawn.js";
import createCRUDroutes from "@/networking/crud.base";

const crudRoutes = createCRUDroutes(
  new Object() as CreateSpawn,
  new Object() as Spawn,
  new Object() as UpdateSpawn,
  "spawn"
);

export default {
  create: crudRoutes.create,
  list: crudRoutes.list,
  read: crudRoutes.read,
  update: crudRoutes.update,
  delete: crudRoutes.delete,
};
