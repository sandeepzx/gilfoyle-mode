# Session 1: Users, Groups and Permissions

## 1. Inspecting User Information

### `id username`

Displays a user's numeric UID, primary GID, and supplementary group memberships.

```bash
id alice
```

Example output:

```text
uid=1001(alice) gid=1001(alice) groups=1001(alice),1002(developers)
```

- `uid=1001(alice)` — Alice's user ID.
- `gid=1001(alice)` — Alice's primary group ID.
- `groups=...` — her primary and supplementary groups.

**Use it when:** Checking which groups a user belongs to and understanding which group permissions may apply.

### `getent passwd username`

Retrieves a user's account record from the system's configured account sources.

```bash
getent passwd alice
```

Example output:

```text
alice:x:1001:1001::/home/alice:/bin/sh
```

The fields, in order, are:

1. Username
2. Password placeholder (`x` usually indicates password information is stored separately)
3. UID
4. Primary GID
5. Optional user description (GECOS)
6. Home directory
7. Login shell

**Use it when:** Checking the configured home directory, login shell, UID, or primary GID.

Note: An account record does not guarantee that its home directory exists or that the user can log in.

---

## 2. Inspecting Groups

### `getent group groupname`

Retrieves a group's record from the system's configured account sources.

```bash
getent group developers
```

Example output:

```text
developers:x:1002:alice,bob
```

The fields are:

1. Group name
2. Password placeholder
3. Numeric GID
4. Comma-separated supplementary member list

**Use it when:** Checking whether a group exists, its GID, and which users are explicitly listed as supplementary members.

### Primary versus supplementary membership

A user has one primary group and may have multiple supplementary groups.

- **Primary group:** Recorded as the GID in the user's account record.
- **Supplementary group:** An additional group membership.

For example:

```text
uid=1001(alice) gid=1001(alice) groups=1001(alice),1002(developers)
```

Here, `alice` is the primary group and `developers` is supplementary.

The output of `getent group alice` may have an empty member field even though Alice's primary group is `alice`. The group record's member field lists supplementary members, not every user whose primary GID matches that group.

### Example: Inspect the `adm` group

```bash
getent group adm
```

Example:

```text
adm:x:4:syslog,sandeep
```

This identifies `adm` as the group name, `4` as its GID, and `syslog` and `sandeep` as explicitly listed supplementary members.

On Ubuntu, `adm` is commonly associated with access to certain system logs.

---

## 3. Checking a Home Directory

### `ls -ld /home/alice`

```bash
ls -ld /home/alice
```

Displays the directory itself, including its permissions and ownership.

- `ls` — list information.
- `-l` — long format, including permissions and ownership.
- `-d` — show the directory itself instead of listing its contents.

Example:

```text
drwxr-x--- 2 alice alice 4096 Oct 13 10:00 /home/alice
```

This shows that the directory exists, is owned by Alice, belongs to the `alice` group, and has permission mode `750`.

If the path does not exist, the command reports an error.

**Important distinction:**

- `getent passwd alice` shows the home directory configured in Alice's account record.
- `ls -ld /home/alice` checks the actual directory's existence, permissions, and ownership.

A user account can exist even when its home directory is missing.

---

## 4. Creating Groups and Users

### `sudo groupadd groupname`

Creates a new group.

```bash
sudo groupadd backend
```

- `sudo` — requests administrative privileges.
- `groupadd` — creates a group.
- `backend` — the new group's name.

If the group already exists, the command will fail rather than create a duplicate group.

### `sudo useradd -m username`

Creates a user account and requests creation of a home directory.

```bash
sudo useradd -m alice
```

- `useradd` — creates the user account.
- `-m` — creates the home directory.
- `alice` — the username.

The resulting home directory is commonly `/home/alice`, depending on system configuration.

Creating the account does not necessarily set a password or enable password-based login.

### `sudo passwd username`

Sets or changes a user's password interactively.

```bash
sudo passwd alice
```

Use this when you need to set or reset Alice's password and have the required administrative privileges.

---

## 5. Adding Users to Supplementary Groups

### `sudo usermod -aG groupname username`

Adds an existing user to a supplementary group without replacing their other supplementary group memberships.

```bash
sudo usermod -aG developers alice
```

- `usermod` — modifies an existing user account.
- `-a` — append the group to the existing supplementary group memberships.
- `-G developers` — specify the supplementary group.
- `alice` — the user to modify.

### The difference between `-G` and `-aG`

**Without `-a`:**

```bash
sudo usermod -G developers alice
```

Sets Alice's supplementary group list to the specified groups. If other supplementary groups were present, they may be removed from her list.

**With `-aG`:**

```bash
sudo usermod -aG developers alice
```

Adds `developers` while preserving her existing supplementary group memberships.

**Rule to remember:** When adding a supplementary group to an existing user, use `-aG` unless you intentionally want to replace the supplementary group list.

### Verify the change

```bash
id alice
getent group developers
```

- `id alice` — checks Alice's UID, primary GID, and supplementary groups.
- `getent group developers` — checks the group record and its explicitly listed supplementary members.

An existing login session may not immediately receive updated group memberships. A new login session is normally needed for the updated membership to apply to new processes.

**Security note:** Adding a user to a group does not automatically grant access to every file or directory. The relevant permissions, ownership, ACLs, and other access controls must also permit access.

---

## 6. Quick Command Reference

| Command | Purpose |
|---|---|
| `id alice` | Inspect a user's UID and group memberships |
| `getent passwd alice` | Inspect the configured user-account record |
| `getent group developers` | Inspect a group's record and listed supplementary members |
| `getent group adm` | Inspect the `adm` group |
| `ls -ld /home/alice` | Check a home directory's existence, permissions, and ownership |
| `sudo groupadd backend` | Create a group |
| `sudo useradd -m alice` | Create a user and request a home directory |
| `sudo passwd alice` | Set or change a user's password |
| `sudo usermod -aG developers alice` | Add a user to a supplementary group safely |
| `sudo usermod -G developers alice` | Replace the supplementary group list with the specified group list |

## 7. Recommended Inspection Workflow

When checking a user and their home directory, start with read-only inspection:

```bash
id alice
getent passwd alice
ls -ld /home/alice
```

If investigating a group:

```bash
getent group developers
```

After an intentional account or group change, verify the resulting state rather than assuming the command succeeded.

**Core principle:** Linux identifies users and groups by numeric IDs. Names make those IDs easier for people to understand. Group membership influences which group permissions can apply, but access still depends on the permissions and access controls of the relevant files and directories.

## 8. Reading Linux File Permissions

### 8.1 Understanding `ls -l` Output

Example output:

```text
-rw-r----- 1 sandeep developers 120 Oct 13 10:00 report.txt
```

The fields describe the file:

- `-rw-r-----` — file type and permissions.
- `1` — hard-link count.
- `sandeep` — owner.
- `developers` — group owner.
- `120` — file size in bytes.
- `Oct 13 10:00` — modification time.
- `report.txt` — filename.

The first character identifies the file type:

- `-` — regular file.
- `d` — directory.
- `l` — symbolic link.

The next nine characters represent permissions for three classes: owner, group, and others.

For this example:

```text
-rw-r-----
 ||| ||| |||
 ||| ||| +++--- Others
 ||| +++------- Group
 +++----------- Owner
```

- Owner: `rw-` — read and write.
- Group: `r--` — read only.
- Others: `---` — no permissions.

### 8.2 File Permissions: Read, Write, and Execute

For regular files:

- `r` — read the file's contents.
- `w` — modify the file's contents.
- `x` — execute the file, provided it is executable and the other execution requirements are satisfied.

A file's execute permission does not automatically make it a valid executable program. Its contents, interpreter or binary format, and other execution conditions also matter.

### 8.3 Directory Permissions

For directories:

- `r` — list the names of entries inside the directory.
- `w` — create, remove, or rename entries, subject to other restrictions.
- `x` — search or traverse the directory, allowing access to entries when their names are known.

Directory execute permission is especially important. Without it, a user generally cannot access entries inside that directory, even if the user knows a filename.

To access `/home/sandeep/project/file.txt`, the process needs the necessary search (`x`) permission on the directories along the path, as well as the relevant permission on the file itself.

**Important distinction:** File permissions control operations on file contents. Directory permissions control operations on directory entries and traversal.

---

## 9. Changing Permissions, Owners, and Groups

### 9.1 Numeric Permissions

Linux represents the standard permissions using numbers:

| Permission | Value |
|---|---:|
| Read (`r`) | 4 |
| Write (`w`) | 2 |
| Execute (`x`) | 1 |
| None (`---`) | 0 |

Add the values in each permission group to obtain its numeric representation.

- `rwx` = 4 + 2 + 1 = 7.
- `rw-` = 4 + 2 = 6.
- `r-x` = 4 + 1 = 5.
- `r--` = 4.
- `---` = 0.

For example:

```bash
chmod 754 script.sh
```

This sets:

```text
Owner:  7 = rwx
Group:  5 = r-x
Others: 4 = r--
```

Another example:

```bash
chmod 640 report.txt
```

This means the owner can read and write, the group can read, and others have no permissions.

### 9.2 Symbolic Permissions

Symbolic permissions let you modify selected permissions without specifying the entire numeric mode.

Permission classes:

- `u` — owner (user).
- `g` — group.
- `o` — others.
- `a` — all classes.

Operators:

- `+` — add a permission.
- `-` — remove a permission.
- `=` — set the specified permissions for that class.

Examples:

```bash
chmod g+w report.txt    # Add group write permission
chmod o-r report.txt    # Remove others' read permission
chmod u+x script.sh     # Add owner execute permission
chmod g=r report.txt    # Set group permission to read only
```

Be careful with `=`: it replaces the selected class's existing permissions rather than simply adding another permission.

### 9.3 Write Permission Does Not Mean Read Permission

A file can be writable without being readable.

For example, if a user has write permission but no read permission on a file, this command may succeed if the user also has the required directory access:

```bash
echo "New content" > data.txt
```

However, `>` can truncate an existing file before writing the new text. It should not be used casually on important files.

An editor such as `nano` generally needs to read an existing file to display its contents, so editing may behave differently from writing through shell redirection.

### 9.4 Changing the Owner with `chown`

`chown` changes a file's owner and can also change its group.

```bash
sudo chown bob report.txt
```

This changes the owner to `bob`; the group remains unchanged.

```bash
sudo chown bob:developers report.txt
```

This changes both the owner to `bob` and the group to `developers`.

```bash
sudo chown :developers report.txt
```

This changes only the group.

Ordinary users generally cannot transfer a file's ownership to another user. This normally requires root privileges or an appropriate capability.

### 9.5 Changing the Group with `chgrp`

```bash
chgrp developers report.txt
```

This changes the file's group to `developers`, provided the user is permitted to make the change.

An ordinary file owner can generally change the group to a group they belong to, subject to system rules.

### 9.6 Recursive Ownership and Permission Changes

The `-R` option applies a change recursively to a directory and its contents.

```bash
sudo chown -R bob:developers /some/directory
```

This can change ownership of many files and directories.

**Production caution:** Recursive commands can cause significant damage if run against the wrong path. Verify the target carefully before using `chown -R` or recursive `chmod`.

---

## 10. Parent Directory Permissions and the Sticky Bit

### 10.1 Why Parent Directory Permissions Matter

Permissions on a file are only part of the access decision.

Suppose Bob has read permission on `report.txt`, but cannot traverse one of its parent directories. Bob may still be unable to access the file through that path.

When diagnosing an access problem, inspect every directory along the path.

Useful command:

```bash
namei -l /path/to/file
```

This helps reveal ownership and permissions on each component of the path.

### 10.2 Understanding the Sticky Bit

The sticky bit is commonly used on directories that are writable by many users.

Inspect `/tmp`:

```bash
ls -ld /tmp
```

A typical result is:

```text
drwxrwxrwt ... /tmp
```

The final `t` indicates that the sticky bit is set and others have execute permission.

A common numeric mode is:

```bash
chmod 1777 directory
```

The `1` sets the sticky bit, while `777` gives read, write, and execute permissions to owner, group, and others.

In a sticky directory, a user generally cannot delete or rename another user's entry merely because the directory is writable. The entry's owner, the directory's owner, or a privileged user can normally perform that operation.

The sticky bit does **not** protect the file's contents. It restricts deletion and renaming of directory entries.

This explains why an ordinary user may be unable to remove another user's file from `/tmp`, even though `/tmp` is writable by everyone.

---

## 11. Special Permission Bits: setuid, setgid, and Sticky

Linux has three special permission bits in addition to the ordinary `rwx` permissions.

| Special bit | Numeric value | Main purpose |
|---|---:|---|
| setuid | 4 | Can change the effective user identity of an eligible executable process |
| setgid | 2 | Can change the effective group identity of an eligible executable process; on directories, helps control group inheritance |
| sticky | 1 | Restricts deletion and renaming of entries in shared writable directories |

The first digit in a four-digit numeric mode represents these special bits.

Examples:

```text
4755  setuid + 755
2755  setgid + 755
1777  sticky + 777
2775  setgid + 775
```

The special bits can be combined. For example, `3` in the special digit means setgid plus sticky.

### 11.1 setuid

On an eligible executable, setuid can cause the process's effective user ID to become the file owner's user ID.

For example, if Bob executes an eligible setuid executable owned by Sandeep, the process may have:

- Real user ID: Bob.
- Effective user ID: Sandeep.

The real ID identifies the user who launched the process. The effective ID is important for many permission checks.

A familiar system example is `/usr/bin/passwd`, which is commonly installed with setuid enabled so it can perform carefully controlled password updates.

Inspect it without changing anything:

```bash
ls -l /usr/bin/passwd
```

On many Ubuntu installations, its permissions include an `s` in the owner's execute position.

Important limitations:

- setuid does not change the file's owner.
- It does not mean the executable can access every file.
- Linux restricts setuid behavior in some circumstances, including for scripts and on mounts configured with `nosuid`.
- Privileged executables must be designed carefully to avoid security vulnerabilities.

**Never set setuid on a random program as an experiment.**

### 11.2 setgid on Executables

On an eligible executable, setgid can cause the process's effective group ID to become the file's group.

As with setuid, actual behavior depends on Linux execution rules and filesystem or mount configuration.

### 11.3 setgid on Directories

On a directory, setgid is particularly useful for shared project folders.

Normally, a newly created file receives a group based on the creator's group and the applicable system rules. In a setgid directory, new files and subdirectories normally inherit the directory's group.

For example, a team might use a shared directory owned by the `developers` group. Setting setgid on that directory helps newly created files remain associated with the `developers` group.

```bash
chmod g+s shared
```

Or numerically:

```bash
chmod 2775 shared
```

The resulting mode commonly appears as:

```text
drwxrwsr-x
```

The `s` in the group execute position indicates setgid and group execute permission.

**Important:** setgid does not automatically make every new file group-writable. The file creation mode, the creator's `umask`, and any ACLs still affect the final permissions.

### 11.4 Uppercase `S` and Lowercase `s`

The letter in the permission string shows both the special bit and the associated execute permission.

- Lowercase `s` — the special bit is set and the associated execute permission is enabled.
- Uppercase `S` — the special bit is set but the associated execute permission is disabled.

For example:

```text
-rwsr-xr-x
```

Here, setuid is set and owner execute permission is enabled.

```text
-rwSr-xr-x
```

Here, setuid is set but owner execute permission is disabled. The file cannot be executed by its owner through ordinary execute permission.

Similarly, a directory shown as:

```text
drwxrwSr-x
```

has setgid set, but group execute permission is absent. Members relying on group access generally cannot traverse the directory.

The uppercase letter does not represent a stronger privilege. It indicates that the special bit is set while the corresponding execute bit is absent.

### 11.5 Sticky Bit: `t` and `T`

The same display principle applies to the sticky bit.

- Lowercase `t` — sticky bit set and others' execute permission enabled.
- Uppercase `T` — sticky bit set but others' execute permission disabled.

A typical shared temporary directory looks like this:

```text
drwxrwxrwt
```

A directory with `T` instead of `t` has the sticky bit enabled but lacks others' execute permission. Users relying on others' permissions generally cannot traverse it.

### 11.6 Special-Bit Examples

```bash
chmod 4755 file
chmod 2755 directory
chmod 1777 directory
chmod 2775 shared
```

Interpretation:

- `4755`: setuid plus owner `rwx`, group `r-x`, others `r-x`.
- `2755`: setgid plus owner `rwx`, group `r-x`, others `r-x`.
- `1777`: sticky plus `rwx` for all classes.
- `2775`: setgid plus owner `rwx`, group `rwx`, others `r-x`.

The first digit controls the special bits, while the remaining three digits control ordinary permissions.

---

## 12. Safe Permission-Lab Practices

Use temporary directories for experiments instead of changing permissions on system directories or important personal files.

For example:

```bash
mkdir -p /tmp/linux-permission-lab
cd /tmp/linux-permission-lab
pwd
ls -ld .
```

This creates a temporary lab directory, moves into it, displays its absolute path, and inspects the directory itself.

When testing permissions:

1. Inspect the current owner, group, and mode before making changes.
2. Change only files or directories created for the experiment.
3. Use `ls -l`, `ls -ld`, and `getfacl` when appropriate to verify the result.
4. Test access as the intended user where practical.
5. Restore the original permissions and ownership when finished.
6. Avoid experimenting with setuid on custom executables.
7. Never recursively change permissions or ownership on system directories as a learning exercise.

Temporary directories can be removed when the experiment is complete, but verify the exact path first.

```bash
pwd
ls -la /tmp/linux-permission-lab
```

Only after confirming the target is the lab directory should you clean it up:

```bash
rm -r /tmp/linux-permission-lab
```

---

## 13. Permission Troubleshooting Workflow

When a user cannot read, write, execute, create, or delete something, inspect the relevant permissions in a consistent order.

### Step 1: Identify the User and Groups

```bash
id username
```

This reveals the user's UID, primary GID, and supplementary groups.

### Step 2: Inspect the File or Directory

```bash
ls -l /path/to/file
ls -ld /path/to/directory
```

Check the owner, group, ordinary permissions, and special bits.

### Step 3: Inspect Parent Directories

```bash
namei -l /path/to/file
```

Check whether the user can traverse each directory in the path.

### Step 4: Identify the Operation That Failed

Ask what the user was trying to do:

- Read file contents?
- Modify file contents?
- Execute a program?
- List a directory?
- Create a new entry?
- Delete or rename an entry?

Different operations require different permissions.

### Step 5: Check Special Cases

Look for:

- A sticky bit that restricts deletion or renaming.
- setuid or setgid behavior.
- Read-only filesystems or mounts.
- Other security mechanisms that may deny access.

### Step 6: Make the Smallest Appropriate Change

Avoid making everything world-writable with `chmod 777`. Instead, grant only the permissions required to the appropriate user or group.

### Step 7: Verify

Repeat the relevant inspection and, where practical, test the operation as the intended user.

---

## 14. Quick Reference: Permissions

| Command | Purpose |
|---|---|
| `ls -l file` | Inspect a file's permissions and ownership |
| `ls -ld directory` | Inspect a directory itself |
| `chmod 640 file` | Set ordinary numeric permissions |
| `chmod g+w file` | Add group write permission |
| `chmod o-r file` | Remove others' read permission |
| `chown bob file` | Change the owner |
| `chown bob:developers file` | Change owner and group |
| `chgrp developers file` | Change the group |
| `namei -l /path/to/file` | Inspect permissions along a path |
| `id username` | Inspect UID and group memberships |
| `sudo command` | Run an authorized command with elevated privileges |

### Final Mental Model

Linux access control is not just about the permission string shown by `ls -l`.

To understand whether an operation succeeds, consider:

1. **Identity:** Which user and groups does the process have?
2. **Ownership:** Who owns the file or directory, and which group owns it?
3. **Permissions:** Are the required read, write, or execute permissions available?
4. **Path traversal:** Can the process search each parent directory?
5. **Special bits:** Do setuid, setgid, or sticky-bit rules affect the operation?
6. **Other controls:** Do mount options or additional security mechanisms impose restrictions?

The goal is not to memorize permission strings alone. It is to reason from the process's identity, the operation it wants to perform, and the rules governing every relevant filesystem component.

# 15. Access Control Lists (ACLs)

Standard Linux permissions divide access into three classes:

- **Owner** — the file's owning user (`user::`)
- **Owning group** — the file's owning group (`group::`)
- **Others** — users who do not match the owner or group classes (`other::`)

ACLs extend this model by allowing permissions for specific users and groups without changing the file's owner or owning group.

For example, `user:bob:r--` grants Bob read permission through a named-user ACL entry.

## Inspecting ACLs with `getfacl`

Use `getfacl` to display a file or directory's ACL:

```bash
getfacl report.txt
```

Example output:

```text
user::rw-
user:bob:r--
group::rw-
mask::rw-
other::r--
```

Interpretation:

- `user::rw-` — the owner can read and write.
- `user:bob:r--` — Bob's ACL entry allows reading.
- `group::rw-` — the owning group's entry allows reading and writing, subject to the mask.
- `mask::rw-` — the maximum effective permissions for mask-controlled entries.
- `other::r--` — others can read.

## Adding or Changing ACL Entries with `setfacl`

Use `setfacl -m` to modify an ACL:

```bash
setfacl -m u:bob:r-- report.txt
setfacl -m g:developers:r-- report.txt
```

Here:

- `u:bob:r--` adds read permission for the named user Bob.
- `g:developers:r--` adds read permission for the named group `developers`.

Check the result:

```bash
getfacl report.txt
```

ACLs extend normal Linux permission checks; they do not bypass all other security restrictions.

---

# 16. ACL Masks and Effective Permissions

The ACL mask limits the effective permissions of:

- The owning group entry (`group::`)
- Named-user entries (`user:bob:`)
- Named-group entries (`group:developers:`)

The mask does **not** limit the owner entry (`user::`) or the others entry (`other::`).

## How Effective Permissions Work

For an entry controlled by the mask:

**Effective permissions = ACL entry permissions intersected with the mask.**

A permission is effective only when both the entry and the mask allow it.

The mask can restrict permissions, but it cannot grant a permission that the ACL entry itself does not contain.

### Examples

| ACL entry | Mask | Effective permissions |
|---|---|---|
| `rwx` | `r-x` | `r-x` |
| `rw-` | `rwx` | `rw-` |
| `r--` | `rwx` | `r--` |
| `rwx` | `r--` | `r--` |

For example:

```text
user::rwx
user:bob:rwx
group::r--
mask::r--
other::---
```

The effective permissions are:

- **Owner:** `rwx` — the mask does not limit the owner.
- **Bob:** `r--` — Bob's `rwx` entry is restricted by the `r--` mask.
- **Owning group:** `r--` — the mask also restricts the owning-group entry.

`getfacl` may display comments such as `#effective:r--` when an entry's stored permissions exceed its effective permissions.

## How the Mask Is Calculated

When you add or modify extended ACL entries with `setfacl -m`, the mask is normally recalculated automatically unless you explicitly set it or disable recalculation with `-n`.

Normally, the mask reflects the union of permissions in the owning-group, named-user, and named-group entries. The owner and others entries do not determine the mask.

For example:

```text
user::rw-
user:bob:r--
group::rw-
mask::rw-
other::r--
```

The mask is `rw-` because the owning-group entry grants `rw-`, while Bob's entry grants `r--`. Combining these permissions produces `rw-`.

### Important Consequence

Changing the mask can affect several entries at once.

An ACL entry may retain permissions that are temporarily restricted by the mask. If the mask is later increased, some of those previously restricted permissions can become effective again.

Remember:

- The ACL entry defines the permissions assigned to that entry.
- The mask defines the maximum effective permissions for mask-controlled entries.
- The effective permissions are the intersection of the two.

---

# 17. Default ACLs and Inheritance

An **access ACL** controls access to the file or directory on which it is set.

A **default ACL** can be set only on a directory. It acts as a template for permissions on newly created children.

## Setting a Default ACL

Example:

```bash
setfacl -m d:u:bob:r-x shared/
```

This adds a default ACL entry for Bob to the `shared/` directory.

## What Gets Inherited?

- Newly created files can inherit access ACL entries from the parent directory's default ACL.
- Newly created subdirectories can inherit access ACL entries and the parent's default ACL.
- Inherited default ACLs on subdirectories can be passed on to their own children.
- Regular files do not receive `default:` entries themselves.
- Adding a default ACL does not retroactively change existing children.

### Directory Example

A directory might contain:

```text
user::rwx
user:bob:r-x
group::rwx
mask::rwx
other::r-x
default:user::rwx
default:user:bob:r-x
default:group::rwx
default:mask::rwx
default:other::r-x
```

The regular entries control access to the current directory.

The `default:` entries define the ACL template inherited by newly created children.

## Creation Mode Matters

Inherited ACL permissions are adjusted to the mode requested by the program creating the object.

For example, programs commonly create regular files with a mode that does not include execute permission. Therefore, a default ACL containing execute permission does not automatically make every new regular file executable.

A newly created file might show:

```text
user::rw-
user:bob:r-x       #effective:r--
group::rwx         #effective:rw-
mask::rw-
other::r--
```

Here:

- Bob's stored ACL entry is `r-x`.
- The mask is `rw-`.
- Bob's effective permissions are `r--`.
- The owning group's stored entry is `rwx`, but its effective permissions are `rw-`.
- The file has no `default:` entries because it is a regular file.

The creation mode affects the inherited permissions, and the mask limits the effective permissions of the relevant ACL entries.

---

# 18. Testing and Troubleshooting ACLs Safely

Use a dedicated test directory rather than experimenting on system files or important personal data.

## Inspecting an ACL

```bash
getfacl report.txt
```

This displays the ACL entries and, when relevant, effective-permission comments.

## Adding a Read-Only Entry for Bob

```bash
setfacl -m u:bob:r-- report.txt
```

Bob's named-user ACL entry now specifies read permission.

## Testing a Write Attempt as Bob

```bash
sudo -u bob sh -c 'echo "Bob was here" >> report.txt'
```

If Bob's effective ACL permissions are read-only, the append should be denied.

The file's parent directories must also be accessible to Bob. A user needs appropriate directory traversal permissions to reach the file, even when the file's ACL itself permits reading or writing.

## ACL Troubleshooting Workflow

When a user cannot access a file:

1. **Inspect the ACL.**

   ```bash
   getfacl report.txt
   ```

2. **Identify the applicable entry.** Determine whether access is controlled by the owner, a named user, the owning group, a named group, or others.

3. **Check the mask.** For mask-controlled entries, compare the entry's permissions with `mask::` to determine the effective permissions.

4. **Check parent directories.** A user may lack the directory permissions needed to reach the file.

5. **Check inheritance.** For newly created children, inspect the parent directory's default ACL and consider the creation mode.

6. **Test as the intended user.** Use a controlled test command and inspect the ACL again.

---

# Session 1 Completion

**Session 1 — Users, Groups and Permissions — is complete.**

Topics covered:

- Inspecting and managing users and groups
- Standard file and directory permissions
- Changing permissions, ownership, and groups
- Parent-directory permissions and the sticky bit
- Special permission bits: setuid, setgid, and sticky
- Safe permission-lab practices
- Permission troubleshooting
- ACL entries for named users and groups
- ACL masks and effective permissions
- Default ACLs and inheritance
- Practical ACL testing and troubleshooting
