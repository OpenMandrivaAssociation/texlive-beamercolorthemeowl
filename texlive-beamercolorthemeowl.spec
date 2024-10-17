Name:		texlive-beamercolorthemeowl
Version:	40105
Release:	2
Summary:	A flexible beamer color theme to maximize visibility
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamercolorthemeowl
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamercolorthemeowl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamercolorthemeowl.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamercolorthemeowl.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a flexible dark or light colour theme
designed for maximum readability in environments where most
themes fall flat. Main features: Dark color theme for
presenting in low-light conditions. Optional light color theme
for presenting in bright ambient light. Redefines color names
"red", "green", "blue", "yellow" to values that are visible
when displayed by certain projectors, particularly those with a
very bright green channel and dim red and blue channels. This
behaviour can be optionally disabled, with the provided colours
also available as "OwlRed", "OwlGreen", etc.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/beamercolorthemeowl
%{_texmfdistdir}/tex/latex/beamercolorthemeowl
%doc %{_texmfdistdir}/doc/latex/beamercolorthemeowl

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
