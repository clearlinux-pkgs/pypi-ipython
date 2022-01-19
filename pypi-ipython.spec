#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ipython
Version  : 8.0.1
Release  : 109
URL      : https://files.pythonhosted.org/packages/c2/4f/67e0c9ab885a5ba54b6dfe5f630df70b73a2de5ef04c402e0691c1936273/ipython-8.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/c2/4f/67e0c9ab885a5ba54b6dfe5f630df70b73a2de5ef04c402e0691c1936273/ipython-8.0.1.tar.gz
Summary  : IPython: Productive Interactive Computing
Group    : Development/Tools
License  : BSD-3-Clause BSD-3-Clause-Clear
Requires: pypi-ipython-bin = %{version}-%{release}
Requires: pypi-ipython-license = %{version}-%{release}
Requires: pypi-ipython-man = %{version}-%{release}
Requires: pypi-ipython-python = %{version}-%{release}
Requires: pypi-ipython-python3 = %{version}-%{release}
Requires: pypi(backcall)
Requires: pypi(pexpect)
Requires: pypi(pygments)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(backcall)
BuildRequires : pypi(black)
BuildRequires : pypi(colorama)
BuildRequires : pypi(decorator)
BuildRequires : pypi(jedi)
BuildRequires : pypi(matplotlib_inline)
BuildRequires : pypi(pexpect)
BuildRequires : pypi(pickleshare)
BuildRequires : pypi(prompt_toolkit)
BuildRequires : pypi(pygments)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(stack_data)
BuildRequires : pypi(traitlets)
BuildRequires : pypi(wheel)

%description
.. image:: https://codecov.io/github/ipython/ipython/coverage.svg?branch=master
:target: https://codecov.io/github/ipython/ipython?branch=master

%package bin
Summary: bin components for the pypi-ipython package.
Group: Binaries
Requires: pypi-ipython-license = %{version}-%{release}

%description bin
bin components for the pypi-ipython package.


%package license
Summary: license components for the pypi-ipython package.
Group: Default

%description license
license components for the pypi-ipython package.


%package man
Summary: man components for the pypi-ipython package.
Group: Default

%description man
man components for the pypi-ipython package.


%package python
Summary: python components for the pypi-ipython package.
Group: Default
Requires: pypi-ipython-python3 = %{version}-%{release}

%description python
python components for the pypi-ipython package.


%package python3
Summary: python3 components for the pypi-ipython package.
Group: Default
Requires: python3-core
Provides: pypi(ipython)
Requires: pypi(backcall)
Requires: pypi(black)
Requires: pypi(colorama)
Requires: pypi(decorator)
Requires: pypi(jedi)
Requires: pypi(matplotlib_inline)
Requires: pypi(pexpect)
Requires: pypi(pickleshare)
Requires: pypi(prompt_toolkit)
Requires: pypi(pygments)
Requires: pypi(setuptools)
Requires: pypi(stack_data)
Requires: pypi(traitlets)

%description python3
python3 components for the pypi-ipython package.


%prep
%setup -q -n ipython-8.0.1
cd %{_builddir}/ipython-8.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642607220
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ipython
cp %{_builddir}/ipython-8.0.1/COPYING.rst %{buildroot}/usr/share/package-licenses/pypi-ipython/f8e8135e4c13eb9436ff08f23dbd3362be77a543
cp %{_builddir}/ipython-8.0.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ipython/68f5a6f2199e7779b637c326af87d70ef6ee6222
cp %{_builddir}/ipython-8.0.1/docs/source/about/license_and_copyright.rst %{buildroot}/usr/share/package-licenses/pypi-ipython/7ababbc82643a97634faa381d823f624683844c0
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
#python kernel install --prefix %{buildroot}/usr
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ipython
/usr/bin/ipython3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-ipython/68f5a6f2199e7779b637c326af87d70ef6ee6222
/usr/share/package-licenses/pypi-ipython/7ababbc82643a97634faa381d823f624683844c0
/usr/share/package-licenses/pypi-ipython/f8e8135e4c13eb9436ff08f23dbd3362be77a543

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ipython.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
