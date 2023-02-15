export interface Spawn {
  id: number;
  strain: string;
  inoculation_type: string;
  inoculation_date: string;
  full_colonization_date: string;
  notes: string;
}

export interface CreateSpawn {
  strain: string;
  inoculation_type: string;
  inoculation_date: string;
  full_colonization_date: string;
  notes: string;
}

export interface UpdateSpawn {
  strain: Optional[string];
  inoculation_type: Optional[string];
  inoculation_date: Optional[string];
  full_colonization_date: Optional[string];
  notes: Optional[string];
}
