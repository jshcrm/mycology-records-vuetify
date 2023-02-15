import type {
  CreateIngredient,
  Ingredient,
  UpdateIngredient,
} from "@/interfaces/Ingredient.js";
import createCRUDroutes from "@/networking/crud.base";

const crudRoutes = createCRUDroutes(
  new Object() as CreateIngredient,
  new Object() as Ingredient,
  new Object() as UpdateIngredient,
  "ingredient"
);

export default {
  list: crudRoutes.list,
  create: crudRoutes.create,
  read: crudRoutes.read,
  update: crudRoutes.update,
  delete: crudRoutes.delete,
};
