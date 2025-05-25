from collections import deque
import time
class Mytree:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, node):
        self.children.append(node)

    def showTree(self, level=0):
        print("  "*level + f"->{self.name}")
        for child in self.children:
            child.showTree(level+1)

    def Dfs_search(self, target):
        if self.name == target:
            return self
        for child in self.children:
            result = child.Dfs_search(target)
            if result:
                return result
        return None
    
    def Bfs_search(self, target):
        queue = deque([self])
        while queue:
            current = queue.popleft()
            if current.name == target:
                return current
            queue.extend(current.children)
        return None

root = Mytree("Menu Utama")

# Level 1
account = Mytree("Account")
setting = Mytree("Setting")
dashboard = Mytree("Dashboard")

# Level 2 - Account
profile = Mytree("Profile")
security = Mytree("Security")

# Level 3 - Profile
edit_profile = Mytree("Edit Profile")
view_profile = Mytree("View Profile")

# Level 4 - Edit Profile
change_name = Mytree("Change Name")
change_photo = Mytree("Change Photo")

# Level 4 - View Profile
view_activity = Mytree("View Activity")

# Level 3 - Security
password = Mytree("Password")
twofa = Mytree("Two-Factor Auth")

# Level 4 - Password
change_pass = Mytree("Change Password")
password_hint = Mytree("Set Password Hint")

# Level 2 - Setting
notif = Mytree("Notification")
display = Mytree("Display")

# Level 3 - Notification
email_notif = Mytree("Email Notification")
push_notif = Mytree("Push Notification")

# Level 3 - Display
theme = Mytree("Theme")
font = Mytree("Font Size")

# Level 2 - Dashboard
tambah = Mytree("Tambah Data")
lihat = Mytree("Lihat Data")

# Level 3 - Tambah Data
import_excel = Mytree("Import Excel")
manual_entry = Mytree("Manual Entry")

# Struktur pohon
root.addChild(account)
root.addChild(setting)
root.addChild(dashboard)

account.addChild(profile)
account.addChild(security)

profile.addChild(edit_profile)
profile.addChild(view_profile)

edit_profile.addChild(change_name)
edit_profile.addChild(change_photo)

view_profile.addChild(view_activity)

security.addChild(password)
security.addChild(twofa)

password.addChild(change_pass)
password.addChild(password_hint)

setting.addChild(notif)
setting.addChild(display)

notif.addChild(email_notif)
notif.addChild(push_notif)

display.addChild(theme)
display.addChild(font)

dashboard.addChild(tambah)
dashboard.addChild(lihat)

tambah.addChild(import_excel)
tambah.addChild(manual_entry)

print(root.showTree())

mulaicari_dfs = time.time()
pencarianDfs = root.Dfs_search("Tambah dat1a")
selesaicari_dfs = time.time()
waktucari_dfs = selesaicari_dfs - mulaicari_dfs
print(f"data ditemukan via DFS: {pencarianDfs.name if pencarianDfs else 'Tidak Ditemukan'}")
print(f"waktu yang dibutuhkan untuk DFS search adalah: {waktucari_dfs * 1000:.3f}")


mulaicari_bfs = time.time()
pencarianBfs = root.Bfs_search("Tambah dat1a")
selesaicari_bfs = time.time()
waktucari_bfs = selesaicari_bfs - mulaicari_bfs
print(f"data ditemukan via BFS: {pencarianBfs.name if pencarianBfs else 'Tidak Ditemukan'}")
print(f"waktu yang dibutuhkan untuk BFS search adalah: {waktucari_bfs * 1000:.3f}")
