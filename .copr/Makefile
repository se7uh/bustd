srpm:
	dnf install -y rpm-build
	mkdir -p $(outdir)
	cp bustd.spec $(outdir)/bustd.spec
	curl -L https://github.com/vrmiguel/bustd/archive/master.tar.gz -o $(outdir)/master.tar.gz 