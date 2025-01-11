srpm:
	dnf install -y rpm-build
	mkdir -p $(outdir)
	cp bustd.spec $(outdir)/bustd.spec
	cp bustd.service $(outdir)/bustd.service
	curl -L https://github.com/vrmiguel/bustd/archive/master.tar.gz -o $(outdir)/master.tar.gz 