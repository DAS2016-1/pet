execute 'apt-get update'
package 'vim'
package 'postgresql-9.4'
package 'postgresql-9.4-debversion'
package 'python-argparse' 
package 'python-debian' 
package 'python-debianbts' 
package 'python-inotifyx' 
package 'python-paste' 
package 'python-psycopg2' 
package 'python-pyramid' 
package 'python-sqlalchemy'
package 'python-subversion'
package 'python-pip' 
package 'wget'

execute 'pip install pyramid_chameleon'

user 'pet' do
  action :create
end

file '/etc/postgresql/9.4/main/postgresql.conf' do
  owner 'postgres'
  group 'postgres'
  mode '644'
  action :create
end

file '/etc/postgresql/9.4/main/pg_hba.conf' do
  owner 'postgres'
  group 'postgres'
  mode '640'
  action :create
end

service 'postgresql' do
  action :start
end

execute "createuser --createdb pet" do
  user "postgres"
  action :run
  ignore_failure true
end

execute "createdb pet" do
  user "pet"
  action :run
  ignore_failure true
end

execute "psql pet < /usr/share/postgresql/9.4/contrib/debversion.sql" do
  user "postgres"
  action :run
  ignore_failure true
end

file '/etc/hosts' do
  owner 'root'
  group 'root'
  mode '644'
  action :create
end

execute "/vagrant/pet-update -c" do
  user "pet"
  action :run
end

