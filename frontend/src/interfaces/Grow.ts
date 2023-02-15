import type { Media } from "@/interfaces/Media";
import type { Strain } from "@/interfaces/Strain";

export interface Grow {
  id: number;
  strain_id: number;
  strain: Strain;
  medias: Media[];
  notes: string;
}

export interface CreateGrow {
  strain_id: number;
  notes: string;
}

export interface UpdateGrow {
  strain_id: number;
  notes: string;
}
