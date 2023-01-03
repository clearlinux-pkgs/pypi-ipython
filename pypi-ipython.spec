#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-ipython
Version  : 8.8.0
Release  : 128
URL      : https://files.pythonhosted.org/packages/f5/39/89664d8c3e4dfb0a73862cbbff8eb4028a1e3d4305da80ab0a493848ed9b/ipython-8.8.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f5/39/89664d8c3e4dfb0a73862cbbff8eb4028a1e3d4305da80ab0a493848ed9b/ipython-8.8.0.tar.gz
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
.. image:: https://codecov.io/github/ipython/ipython/coverage.svg?branch=main
:target: https://codecov.io/github/ipython/ipython?branch=main

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
Requires: pypi(colorama)
Requires: pypi(decorator)
Requires: pypi(jedi)
Requires: pypi(matplotlib_inline)
Requires: pypi(pexpect)
Requires: pypi(pickleshare)
Requires: pypi(prompt_toolkit)
Requires: pypi(pygments)
Requires: pypi(stack_data)
Requires: pypi(traitlets)

%description python3
python3 components for the pypi-ipython package.


%prep
%setup -q -n ipython-8.8.0
cd %{_builddir}/ipython-8.8.0
pushd ..
cp -a ipython-8.8.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672760944
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-ipython
cp %{_builddir}/ipython-%{version}/COPYING.rst %{buildroot}/usr/share/package-licenses/pypi-ipython/f8e8135e4c13eb9436ff08f23dbd3362be77a543 || :
cp %{_builddir}/ipython-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-ipython/68f5a6f2199e7779b637c326af87d70ef6ee6222 || :
cp %{_builddir}/ipython-%{version}/docs/source/about/license_and_copyright.rst %{buildroot}/usr/share/package-licenses/pypi-ipython/7ababbc82643a97634faa381d823f624683844c0 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
## install_append content
#python kernel install --prefix %{buildroot}/usr
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
