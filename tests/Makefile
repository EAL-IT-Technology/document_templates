all: test.pdf test-notoc.pdf

test.pdf: test.md template/template.tex
	pandoc                          \
	  --from         markdown       \
	  --to           latex          \
	  --template     template/template.tex   \
	  --out          test.pdf \
	  --latex-engine xelatex        \
	  test.md

test-notoc.pdf: test.md template/template-notoc.tex
	pandoc                          \
	  --from         markdown       \
	  --to           latex          \
	  --template     template/template-notoc.tex   \
	  --out          test-notoc.pdf \
	  --latex-engine xelatex        \
	  test.md
