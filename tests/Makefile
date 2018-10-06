all: test.pdf test-notoc.pdf

test.pdf: test.md template/template.tex
	pandoc                          \
	  --from         markdown       \
	  --to           latex          \
	  --template     template/template.tex   \
	  --out          test.pdf       \
	  --pdf-engine   pdflatex       \
	  test.md

test-notoc.pdf: test.md template/template.tex
	pandoc                          \
	  --from         markdown       \
	  --to           latex          \
	  --template     template/template.tex   \
	  --out          test-notoc.pdf \
	  --pdf-engine pdflatex         \
	  --variable="skip-toc=true"    \
	  test.md
