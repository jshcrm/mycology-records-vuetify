import axios from "axios";
import type { AxiosResponse } from "axios";

interface CrudRouter<CreateInterface, ReadInterface, UpdateInterface> {
  list: () => Promise<AxiosResponse<ReadInterface[], any>>;
  read: (id: string) => Promise<AxiosResponse<ReadInterface, any>>;
  create: (
    data: CreateInterface
  ) => Promise<AxiosResponse<ReadInterface[], any>>;
  update: (
    data: UpdateInterface
  ) => Promise<AxiosResponse<ReadInterface[], any>>;
  delete: (id: string) => Promise<AxiosResponse<ReadInterface, any>>;
}

export default function createCRUDroutes<
  CreateInterface,
  ReadInterface,
  UpdateInterface
>(
  createInterface: CreateInterface,
  readInterface: ReadInterface,
  updateInterface: UpdateInterface,
  url: string
): CrudRouter<
  typeof createInterface,
  typeof readInterface,
  typeof updateInterface
> {
  return {
    async create(
      data: typeof createInterface
    ): Promise<AxiosResponse<(typeof readInterface)[]>> {
      return axios.post(`${import.meta.env.VITE_API}/${url}/`, data);
    },
    async list(): Promise<AxiosResponse<(typeof readInterface)[]>> {
      return await axios.get(`${import.meta.env.VITE_API}/${url}/`);
    },
    async read(id: string): Promise<AxiosResponse<typeof readInterface>> {
      return await axios.get(`${import.meta.env.VITE_API}/${url}/${id}/`);
    },
    async update(
      data: typeof updateInterface
    ): Promise<AxiosResponse<(typeof readInterface)[]>> {
      return axios.post(`${import.meta.env.VITE_API}/${url}/${id}/`, data);
    },
    async delete(id: string): Promise<AxiosResponse<typeof readInterface>> {
      return axios.post(`${import.meta.env.VITE_API}/${url}/${id}/`);
    },
  };
}
