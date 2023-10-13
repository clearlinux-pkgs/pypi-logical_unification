#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-logical_unification
Version  : 0.4.6
Release  : 15
URL      : https://files.pythonhosted.org/packages/c0/73/8dac224c46949e61bc52558384138a2b79fa0b7be10367074862fe9994dd/logical-unification-0.4.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/c0/73/8dac224c46949e61bc52558384138a2b79fa0b7be10367074862fe9994dd/logical-unification-0.4.6.tar.gz
Summary  : Logical unification in Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-logical_unification-license = %{version}-%{release}
Requires: pypi-logical_unification-python = %{version}-%{release}
Requires: pypi-logical_unification-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(multipledispatch)
BuildRequires : pypi(toolz)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Logical Unification
[![Build Status](https://travis-ci.org/pythological/unification.svg?branch=main)](https://travis-ci.org/pythological/unification) [![Coverage Status](https://coveralls.io/repos/github/pythological/unification/badge.svg?branch=main)](https://coveralls.io/github/pythological/unification?branch=main) [![PyPI](https://img.shields.io/pypi/v/logical-unification)](https://pypi.org/project/logical-unification/)

%package license
Summary: license components for the pypi-logical_unification package.
Group: Default

%description license
license components for the pypi-logical_unification package.


%package python
Summary: python components for the pypi-logical_unification package.
Group: Default
Requires: pypi-logical_unification-python3 = %{version}-%{release}

%description python
python components for the pypi-logical_unification package.


%package python3
Summary: python3 components for the pypi-logical_unification package.
Group: Default
Requires: python3-core
Provides: pypi(logical_unification)
Requires: pypi(multipledispatch)
Requires: pypi(toolz)

%description python3
python3 components for the pypi-logical_unification package.


%prep
%setup -q -n logical-unification-0.4.6
cd %{_builddir}/logical-unification-0.4.6
pushd ..
cp -a logical-unification-0.4.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1684610641
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-logical_unification
cp %{_builddir}/logical-unification-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-logical_unification/45b077e352c945bbc3dfcc8cfe8aaf4211f2185c || :
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
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-logical_unification/45b077e352c945bbc3dfcc8cfe8aaf4211f2185c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
