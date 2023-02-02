# Using Molecule

How to use molecule for unit testing with a sample playbook

## Role init

Initialize a new role. (You can also use molecule to do it)

```bash
> ansible-galaxy init role1
- Role role1 was created successfully
```

## Molecule

Installing molecule

### Install

```bash
> pip3 install molecule

Collecting molecule
  Downloading molecule-4.0.4-py3-none-any.whl (246 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 246.8/246.8 kB 1.1 MB/s eta 0:00:00
Requirement already satisfied: pluggy<2.0,>=0.7.1 in /opt/homebrew/lib/python3.10/site-packages (from molecule) (1.0.0)
Requirement already satisfied: packaging in /opt/homebrew/lib/python3.10/site-packages (from molecule) (23.0)
Collecting click-help-colors>=0.9
  Downloading click_help_colors-0.9.1-py3-none-any.whl (5.5 kB)
Requirement already satisfied: click<9,>=8.0 in /opt/homebrew/lib/python3.10/site-packages (from molecule) (8.1.3)
Collecting ansible-compat>=2.2.0
  Downloading ansible_compat-3.0.1-py3-none-any.whl (19 kB)
Requirement already satisfied: Jinja2>=2.11.3 in /opt/homebrew/lib/python3.10/site-packages (from molecule) (3.1.2)
Collecting cookiecutter>=1.7.3
  Downloading cookiecutter-2.1.1-py2.py3-none-any.whl (36 kB)
Collecting PyYAML>=5.1
  Downloading PyYAML-6.0-cp310-cp310-macosx_11_0_arm64.whl (173 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 174.0/174.0 kB 4.1 MB/s eta 0:00:00
Collecting rich>=9.5.1
  Downloading rich-13.3.1-py3-none-any.whl (239 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 239.0/239.0 kB 6.9 MB/s eta 0:00:00
Collecting enrich>=1.2.7
  Downloading enrich-1.2.7-py3-none-any.whl (8.7 kB)
Collecting jsonschema>=4.9.1
  Downloading jsonschema-4.17.3-py3-none-any.whl (90 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 90.4/90.4 kB 8.1 MB/s eta 0:00:00
Collecting ansible-core>=2.12
  Downloading ansible_core-2.14.2-py3-none-any.whl (2.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.2/2.2 MB 9.8 MB/s eta 0:00:00
Collecting subprocess-tee>=0.4.1
  Downloading subprocess_tee-0.4.1-py3-none-any.whl (5.1 kB)
Requirement already satisfied: requests>=2.23.0 in /opt/homebrew/lib/python3.10/site-packages (from cookiecutter>=1.7.3->molecule) (2.28.2)
Collecting binaryornot>=0.4.4
  Downloading binaryornot-0.4.4-py2.py3-none-any.whl (9.0 kB)
Collecting python-slugify>=4.0.0
  Downloading python_slugify-8.0.0-py2.py3-none-any.whl (9.5 kB)
Collecting jinja2-time>=0.2.0
  Downloading jinja2_time-0.2.0-py2.py3-none-any.whl (6.4 kB)
Requirement already satisfied: MarkupSafe>=2.0 in /opt/homebrew/lib/python3.10/site-packages (from Jinja2>=2.11.3->molecule) (2.1.2)
Collecting pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0
  Downloading pyrsistent-0.19.3-cp310-cp310-macosx_10_9_universal2.whl (82 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 82.5/82.5 kB 3.7 MB/s eta 0:00:00
Requirement already satisfied: attrs>=17.4.0 in /opt/homebrew/lib/python3.10/site-packages (from jsonschema>=4.9.1->molecule) (22.2.0)
Requirement already satisfied: pygments<3.0.0,>=2.14.0 in /opt/homebrew/lib/python3.10/site-packages (from rich>=9.5.1->molecule) (2.14.0)
Collecting markdown-it-py<3.0.0,>=2.1.0
  Downloading markdown_it_py-2.1.0-py3-none-any.whl (84 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 84.5/84.5 kB 7.8 MB/s eta 0:00:00
Collecting cryptography
  Downloading cryptography-39.0.0-cp36-abi3-macosx_10_12_universal2.whl (5.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.4/5.4 MB 27.0 MB/s eta 0:00:00
Collecting resolvelib<0.9.0,>=0.5.3
  Downloading resolvelib-0.8.1-py2.py3-none-any.whl (16 kB)
Collecting chardet>=3.0.2
  Downloading chardet-5.1.0-py3-none-any.whl (199 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 199.1/199.1 kB 20.0 MB/s eta 0:00:00
Collecting arrow
  Downloading arrow-1.2.3-py3-none-any.whl (66 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 66.4/66.4 kB 6.2 MB/s eta 0:00:00
Collecting mdurl~=0.1
  Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Collecting text-unidecode>=1.3
  Downloading text_unidecode-1.3-py2.py3-none-any.whl (78 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 78.2/78.2 kB 3.3 MB/s eta 0:00:00
Requirement already satisfied: certifi>=2017.4.17 in /opt/homebrew/lib/python3.10/site-packages (from requests>=2.23.0->cookiecutter>=1.7.3->molecule) (2022.12.7)
Requirement already satisfied: urllib3<1.27,>=1.21.1 in /opt/homebrew/lib/python3.10/site-packages (from requests>=2.23.0->cookiecutter>=1.7.3->molecule) (1.26.14)
Requirement already satisfied: charset-normalizer<4,>=2 in /opt/homebrew/lib/python3.10/site-packages (from requests>=2.23.0->cookiecutter>=1.7.3->molecule) (3.0.1)
Requirement already satisfied: idna<4,>=2.5 in /opt/homebrew/lib/python3.10/site-packages (from requests>=2.23.0->cookiecutter>=1.7.3->molecule) (3.4)
Collecting python-dateutil>=2.7.0
  Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 247.7/247.7 kB 23.2 MB/s eta 0:00:00
Collecting cffi>=1.12
  Downloading cffi-1.15.1-cp310-cp310-macosx_11_0_arm64.whl (174 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 174.3/174.3 kB 12.3 MB/s eta 0:00:00
Collecting pycparser
  Downloading pycparser-2.21-py2.py3-none-any.whl (118 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 118.7/118.7 kB 5.3 MB/s eta 0:00:00
Requirement already satisfied: six>=1.5 in /opt/homebrew/lib/python3.10/site-packages (from python-dateutil>=2.7.0->arrow->jinja2-time>=0.2.0->cookiecutter>=1.7.3->molecule) (1.16.0)
Installing collected packages: text-unidecode, resolvelib, subprocess-tee, PyYAML, python-slugify, python-dateutil, pyrsistent, pycparser, mdurl, click-help-colors, chardet, markdown-it-py, jsonschema, cffi, binaryornot, arrow, rich, jinja2-time, cryptography, enrich, cookiecutter, ansible-core, ansible-compat, molecule
Successfully installed PyYAML-6.0 ansible-compat-3.0.1 ansible-core-2.14.2 arrow-1.2.3 binaryornot-0.4.4 cffi-1.15.1 chardet-5.1.0 click-help-colors-0.9.1 cookiecutter-2.1.1 cryptography-39.0.0 enrich-1.2.7 jinja2-time-0.2.0 jsonschema-4.17.3 markdown-it-py-2.1.0 mdurl-0.1.2 molecule-4.0.4 pycparser-2.21 pyrsistent-0.19.3 python-dateutil-2.8.2 python-slugify-8.0.0 resolvelib-0.8.1 rich-13.3.1 subprocess-tee-0.4.1 text-unidecode-1.3
```


```bash
molecule init scenario default -r role1 -d docker      
INFO     Initializing new scenario default...
INFO     Initialized scenario in /Users/samarthya/sourcebox/github.com/ansible/play-one/role1/molecule/default successfully.
```

## Manual changes

You have to change `role1/meta/main.yml` for role name like below before you can run the tests

```yaml
galaxy_info:
  role_name: "role1"
  namespace: samarthya
  author: Saurabh Sharma
  description: This is a sample role for testing
  company: samarthya.me
```

## Run the test `molecule test`

Make sure that the current working directory is set to the role directory when you run the molecule test command. You should be in the same directory as the molecule.yml file.

```ansible
> molecule test 

INFO     default scenario test matrix: dependency, lint, cleanup, destroy, syntax, create, prepare, converge, idempotence, side_effect, verify, cleanup, destroy
INFO     Performing prerun with role_name_check=0...
INFO     Set ANSIBLE_LIBRARY=/Users/samarthya/.cache/ansible-compat/07ffa2/modules:/Users/samarthya/.ansible/plugins/modules:/usr/share/ansible/plugins/modules
INFO     Set ANSIBLE_COLLECTIONS_PATH=/Users/samarthya/.cache/ansible-compat/07ffa2/collections:/Users/samarthya/.ansible/collections:/usr/share/ansible/collections
INFO     Set ANSIBLE_ROLES_PATH=/Users/samarthya/.cache/ansible-compat/07ffa2/roles:/Users/samarthya/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles
INFO     Using /Users/samarthya/.cache/ansible-compat/07ffa2/roles/samarthya.role1 symlink to current repository in order to enable Ansible to find the role using its expected full name.
INFO     Running default > dependency
WARNING  Skipping, missing the requirements file.
WARNING  Skipping, missing the requirements file.
INFO     Running default > lint
INFO     Lint is disabled.
INFO     Running default > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running default > destroy
INFO     Sanity checks: 'docker'

PLAY [Destroy] *****************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=instance)

TASK [Wait for instance(s) deletion to complete] *******************************
ok: [localhost] => (item=instance)

TASK [Delete docker networks(s)] ***********************************************
skipping: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=1    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Running default > syntax

playbook: /Users/samarthya/sourcebox/github.com/ansible/play-one/role1/molecule/default/converge.yml
INFO     Running default > create

PLAY [Create] ******************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Log into a Docker registry] **********************************************
skipping: [localhost] => (item=None) 
skipping: [localhost]

TASK [Check presence of custom Dockerfiles] ************************************
ok: [localhost] => (item={'image': 'quay.io/centos/centos:stream8', 'name': 'instance', 'pre_build_image': True})

TASK [Create Dockerfiles from image names] *************************************
skipping: [localhost] => (item={'image': 'quay.io/centos/centos:stream8', 'name': 'instance', 'pre_build_image': True}) 
skipping: [localhost]

TASK [Synchronization the context] *********************************************
skipping: [localhost] => (item={'image': 'quay.io/centos/centos:stream8', 'name': 'instance', 'pre_build_image': True}) 
skipping: [localhost]

TASK [Discover local Docker images] ********************************************
ok: [localhost] => (item={'changed': False, 'skipped': True, 'skip_reason': 'Conditional result was False', 'item': {'image': 'quay.io/centos/centos:stream8', 'name': 'instance', 'pre_build_image': True}, 'ansible_loop_var': 'item', 'i': 0, 'ansible_index_var': 'i'})

TASK [Build an Ansible compatible image (new)] *********************************
skipping: [localhost] => (item=molecule_local/quay.io/centos/centos:stream8) 
skipping: [localhost]

TASK [Create docker network(s)] ************************************************
skipping: [localhost]

TASK [Determine the CMD directives] ********************************************
ok: [localhost] => (item={'image': 'quay.io/centos/centos:stream8', 'name': 'instance', 'pre_build_image': True})

TASK [Create molecule instance(s)] *********************************************
changed: [localhost] => (item=instance)

TASK [Wait for instance(s) creation to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) creation to complete (300 retries left).
FAILED - RETRYING: [localhost]: Wait for instance(s) creation to complete (299 retries left).
changed: [localhost] => (item={'failed': 0, 'started': 1, 'finished': 0, 'ansible_job_id': '669922472502.97460', 'results_file': '/Users/samarthya/.ansible_async/669922472502.97460', 'changed': True, 'item': {'image': 'quay.io/centos/centos:stream8', 'name': 'instance', 'pre_build_image': True}, 'ansible_loop_var': 'item'})

PLAY RECAP *********************************************************************
localhost                  : ok=6    changed=2    unreachable=0    failed=0    skipped=5    rescued=0    ignored=0

INFO     Running default > prepare
WARNING  Skipping, prepare playbook not configured.
INFO     Running default > converge

PLAY [Converge] ****************************************************************

TASK [Gathering Facts] *********************************************************
ok: [instance]

TASK [Include role1] ***********************************************************

PLAY RECAP *********************************************************************
instance                   : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Running default > idempotence

PLAY [Converge] ****************************************************************

TASK [Gathering Facts] *********************************************************
ok: [instance]

TASK [Include role1] ***********************************************************

PLAY RECAP *********************************************************************
instance                   : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Idempotence completed successfully.
INFO     Running default > side_effect
WARNING  Skipping, side effect playbook not configured.
INFO     Running default > verify
INFO     Running Ansible Verifier

PLAY [Verify] ******************************************************************

TASK [Example assertion] *******************************************************
ok: [instance] => {
    "changed": false,
    "msg": "All assertions passed"
}

PLAY RECAP *********************************************************************
instance                   : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

INFO     Verifier completed successfully.
INFO     Running default > cleanup
WARNING  Skipping, cleanup playbook not configured.
INFO     Running default > destroy

PLAY [Destroy] *****************************************************************

TASK [Set async_dir for HOME env] **********************************************
ok: [localhost]

TASK [Destroy molecule instance(s)] ********************************************
changed: [localhost] => (item=instance)

TASK [Wait for instance(s) deletion to complete] *******************************
FAILED - RETRYING: [localhost]: Wait for instance(s) deletion to complete (300 retries left).
changed: [localhost] => (item=instance)

TASK [Delete docker networks(s)] ***********************************************
skipping: [localhost]

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=2    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0

INFO     Pruning extra files from scenario ephemeral directory
```