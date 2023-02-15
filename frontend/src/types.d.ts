/* eslint-disable prettier/prettier */
// Works correctly
export {}

declare module 'vue' {
  interface ComponentCustomProperties {
    $filters: Record<string, function>;
  }
}
