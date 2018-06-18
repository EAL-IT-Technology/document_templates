generating pdfs
===================


clone the repo to a folder called `template`.

run the following command

```
cd test

pandoc                          \
  --from         markdown       \
  --to           latex          \
  --template     template/template.tex   \
  --out          test.pdf \
  --latex-engine xelatex        \
  test.md

```

replace with your own .md and .pdf file name

