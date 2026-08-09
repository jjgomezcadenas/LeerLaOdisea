#!/usr/bin/env bash

set -euo pipefail

project_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
dry_run=false

usage() {
    printf 'Uso: %s [--dry-run]\n' "$(basename -- "$0")"
    printf 'Elimina auxiliares de LaTeX bajo %s y conserva los PDF.\n' "$project_dir"
}

case "${1:-}" in
    "") ;;
    --dry-run|-n) dry_run=true ;;
    --help|-h)
        usage
        exit 0
        ;;
    *)
        usage >&2
        exit 2
        ;;
esac

find "$project_dir" -type f \
    -not -path "$project_dir/.git/*" \
    \( \
        -name '*.acn' -o -name '*.acr' -o -name '*.alg' \
        -o -name '*.aux' -o -name '*.bbl' -o -name '*.bcf' \
        -o -name '*.blg' -o -name '*.brf' -o -name '*.dvi' \
        -o -name '*.fdb_latexmk' -o -name '*.fls' \
        -o -name '*.glg' -o -name '*.glo' -o -name '*.gls' \
        -o -name '*.glsdefs' -o -name '*.idx' -o -name '*.ilg' \
        -o -name '*.ind' -o -name '*.ist' -o -name '*.loa' \
        -o -name '*.lof' -o -name '*.log' -o -name '*.lot' \
        -o -name '*.maf' -o -name '*.mtc' -o -name '*.mtc0' \
        -o -name '*.nav' -o -name '*.nlo' -o -name '*.nls' \
        -o -name '*.out' -o -name '*.run.xml' -o -name '*.snm' \
        -o -name '*.synctex' -o -name '*.synctex.gz' \
        -o -name '*.synctex(busy)' -o -name '*.toc' \
        -o -name '*.upa' -o -name '*.upb' -o -name '*.vrb' \
        -o -name '*.xdv' -o -name '*.xdy' -o -name '*-blx.bib' \
        -o -name 'missfont.log' \
    \) -print0 |
while IFS= read -r -d '' file; do
    if "$dry_run"; then
        printf 'Se eliminaría: %s\n' "${file#"$project_dir"/}"
    else
        printf 'Eliminando: %s\n' "${file#"$project_dir"/}"
        rm -f -- "$file"
    fi
done
