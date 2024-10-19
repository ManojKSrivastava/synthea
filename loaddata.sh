for file in synthea/output/fhir/*.json; do
  curl -X POST -H "Content-Type: application/fhir+json" \
  --data-binary @"$file" http://localhost:8080/fhir
done

