srpm:
	dnf install -y rpm-build
	mkdir -p $(outdir)
	cp bustd.spec $(outdir)/bustd.spec
	cp bustd.service $(outdir)/bustd.service
	curl -L https://github.com/se7uh/bustd/archive/master.tar.gz -o $(outdir)/bustd-0.1.1.tar.gz 