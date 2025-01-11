Name:           bustd
Version:        0.1.1
Release:        1%{?dist}
Summary:        A system daemon for memory management

License:        MIT
URL:            https://github.com/se7uh/bustd
Source0:        https://github.com/se7uh/bustd/archive/master.tar.gz#/%{name}-%{version}.tar.gz
Source1:        bustd.service

BuildRequires:  gcc
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  systemd-rpm-macros

# Runtime requirements
Requires:       systemd

%description
bustd is a lightweight process killer daemon for out-of-memory scenarios for Linux.

%prep
%autosetup -n %{name}-master

%build
cargo build --release

%install
rm -rf %{buildroot}
install -D -m 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

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