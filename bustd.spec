Name:           bustd
Version:        0.1.1
Release:        1%{?dist}
Summary:        A system daemon for memory management

License:        MIT
URL:            https://github.com/se7uh/bustd
Source0:        %{url}/archive/master.tar.gz

BuildRequires:  gcc
BuildRequires:  cargo
BuildRequires:  rust

%description
bustd is a lightweight process killer daemon for out-of-memory scenarios for Linux.

%prep
%autosetup -n %{name}-master

%build
cargo build --release

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -D -m 644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service

%files
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%changelog
* Wed Mar 13 2024 se7uh <example@email.com>
- Initial package 