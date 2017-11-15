TEMPLATE:=template/template.tex

test.pdf: test.md $(TEMPLATE)
	pandoc                          \
	  --from         markdown       \
	  --to           latex          \
	  --template     $(TEMPLATE)   \
	  --out          test.pdf \
	  --latex-engine xelatex        \
	  test.md
