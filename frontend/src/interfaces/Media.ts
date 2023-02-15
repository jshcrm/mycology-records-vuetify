export interface Media {
  id: number;
  name: string;
  inoculation_type: string;
  inoculation_date: string;
  full_colonization_date?: string;
  notes: string;
}

export interface CreateMedia {
  grow_id: number;
  name: string;
  inoculation_type: string;
  inoculation_date: string;
  full_colonization_date?: string;
  notes: string;
}

export interface UpdateMedia {
  name?: string;
  inoculation_type?: string;
  inoculation_date?: string;
  full_colonization_date?: string;
  notes?: string;
}
