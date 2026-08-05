export function shouldProcessInitialQuery(locationKey, seenKeys) {
  if (!locationKey) return false;

  if (seenKeys.has(locationKey)) return false;

  seenKeys.add(locationKey);
  return true;
}
