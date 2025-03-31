-- Lists all Glam rock bands, ranked by their longevity
SELECT
    band_name,
    IFNULL((IFNULL(split, 2020) - formed), 0) AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', IFNULL(style, '')) > 0
ORDER BY lifespan DESC;
