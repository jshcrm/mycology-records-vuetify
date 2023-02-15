export interface Strain {
  id: number;
  name: string;
  short_name: string;
  notes: string;
}

export interface CreateStrain {
  name: string;
  short_name: string;
  notes: string;
}

export interface UpdateStrain {
  name: string;
  short_name: string;
  notes: string;
}
