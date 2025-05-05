%global debug_package %{nil}

Name:		pnpm
Version:	10.10.0
Release:    1
Summary:        Fast, disk space efficient package manager
License:        MIT
Group:          Development/Languages/Other
URL:            https://pnpm.io/
Source0:         https://registry.npmjs.org/%{name}/-/%{name}-%{version}.tgz

BuildRequires:  fdupes
BuildRequires:  nodejs
BuildRequires:  nodejs-packaging
Requires:       bash
Recommends:     python3
Provides:       npm(%{name}) = %{version}
BuildArch:      noarch
%description
pnpm is a package manager for node.js

%package bash-completion
Summary:        Bash completion for %{name}
Group:          System/Shells
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Group:          System/Shells
Requires:       zsh
Supplements:    (%{name} and zsh)

%description zsh-completion
Zsh command line completion support for %{name}.

%package fish-completion
Summary:        Fish completion for %{name}
Group:          System/Shells
Requires:       fish
Supplements:    (%{name} and fish)

%description fish-completion
Fish command line completion support for %{name}.

%prep
%setup -q -n package


%install
%nodejs_install

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
%{buildroot}%{_bindir}/pnpm completion bash > %{buildroot}%{_datadir}/bash-completion/completions/%{name}
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
%{buildroot}%{_bindir}/pnpm completion zsh > %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
%{buildroot}%{_bindir}/pnpm completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish

# Non-Linux files
rm -rf %{buildroot}%{nodejs_sitelib}/pnpm/dist/vendor
rm -f %{buildroot}%{nodejs_sitelib}/pnpm/dist/reflink.{darwin,win32}*.node
rm -f %{buildroot}%{nodejs_sitelib}/pnpm/dist/node_modules/node-gyp/macOS_*
find %{buildroot}%{nodejs_sitelib}/pnpm/dist -type f \
    \( -name '*.cmd' -o -name '*.bat' -o -name '*.ps1' \) -delete

%fdupes %{buildroot}

%files
%license LICENSE
%doc README.md
%{_bindir}/pnp{m,x}
%{nodejs_sitelib}

%files bash-completion
%{_datadir}/bash-completion/

%files zsh-completion
%{_datadir}/zsh/

%files fish-completion
%{_datadir}/fish/
