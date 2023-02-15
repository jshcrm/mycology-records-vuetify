export interface Ingredient {
  id: number;
  name: string;
  amount: string;
}

export interface CreateIngredient {
  name: string;
  amount: string;
}

export interface UpdateIngredient {
  name: string;
  amount: string;
}
