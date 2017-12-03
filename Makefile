BASEDIR=$(CURDIR)
OUTPUTDIR=$(BASEDIR)/out
INPUTDIR=$(BASEDIR)/src


clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

build:
	cd $(INPUTDIR) && \
	find . -name *.rst -readable | cut -sd / -f 2- | \
	xargs -I '{}' -n 1 "rst2html5 {} $(OUTPUTDIR)/{}"
