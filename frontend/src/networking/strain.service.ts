import type {
  Strain,
  CreateStrain,
  UpdateStrain,
} from "@/interfaces/Strain.js";
import createCRUDroutes from "@/networking/crud.base";

const crudRoutes = createCRUDroutes(
  new Object() as CreateStrain,
  new Object() as Strain,
  new Object() as UpdateStrain,
  "strain"
);

export default {
  list: crudRoutes.list,
  create: crudRoutes.create,
  read: crudRoutes.read,
  update: crudRoutes.update,
  delete: crudRoutes.delete,
};
