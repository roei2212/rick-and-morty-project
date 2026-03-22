{{- define "rickmorty-service.name" -}}
rickmorty-service
{{- end }}

{{- define "rickmorty-service.fullname" -}}
{{ include "rickmorty-service.name" . }}
{{- end }}