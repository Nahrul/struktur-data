from collections import deque
import time
class Mytree:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, node):
        self.children.append(node)

    def showTree(self, level=0):
        print("-"*level + f"->{self.name}")
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
root.addChild(account)

# Level 2
profile = Mytree("Profile")
account.addChild(profile)

# Level 3
edit = Mytree("Edit")
profile.addChild(edit)

# Level 4
edit_name = Mytree("Edit Name")
edit_email = Mytree("Edit Email")
edit.addChild(edit_name)
edit.addChild(edit_email)

# Level 5
confirm_name = Mytree("Confirm Name")
save_name = Mytree("Save Name")
edit_name.addChild(confirm_name)
edit_name.addChild(save_name)

# Level 6
name_history = Mytree("Name Change History")
confirm_name.addChild(name_history)

# Depth: 6 reached — continuing horizontally a bit
# Add more vertical chains like above

# === Second Deep Chain ===
security = Mytree("Security")
account.addChild(security)

password = Mytree("Password")
security.addChild(password)

change_password = Mytree("Change Password")
password.addChild(change_password)

input_old = Mytree("Input Old Password")
input_new = Mytree("Input New Password")
change_password.addChild(input_old)
change_password.addChild(input_new)

verify_new = Mytree("Verify New Password")
input_new.addChild(verify_new)

log_event = Mytree("Log Password Change")
verify_new.addChild(log_event)

# === Third Deep Chain ===
setting = Mytree("Setting")
root.addChild(setting)

display = Mytree("Display")
setting.addChild(display)

theme = Mytree("Theme")
display.addChild(theme)

choose_dark = Mytree("Dark Mode")
choose_light = Mytree("Light Mode")
theme.addChild(choose_dark)
theme.addChild(choose_light)

transition = Mytree("Enable Transition")
choose_dark.addChild(transition)

# === Fourth Deep Chain ===
dashboard = Mytree("Dashboard")
root.addChild(dashboard)

tambah_data = Mytree("Tambah Data")
dashboard.addChild(tambah_data)

manual_entry = Mytree("Manual Entry")
tambah_data.addChild(manual_entry)

validate = Mytree("Validasi Form")
manual_entry.addChild(validate)

save = Mytree("Simpan Data")
validate.addChild(save)

log_add = Mytree("Log Tambah")
save.addChild(log_add)

# === Add shorter side branches to reach 50 nodes ===
notif = Mytree("Notification")
setting.addChild(notif)

email_notif = Mytree("Email Notification")
notif.addChild(email_notif)

push_notif = Mytree("Push Notification")
notif.addChild(push_notif)

contact = Mytree("Contact")
root.addChild(contact)

help = Mytree("Help")
root.addChild(help)

faq = Mytree("FAQ")
help.addChild(faq)

about = Mytree("About")
help.addChild(about)

report = Mytree("Report")
root.addChild(report)

monthly = Mytree("Monthly")
report.addChild(monthly)

export_pdf = Mytree("Export PDF")
monthly.addChild(export_pdf)


print(root.showTree())

mulaicari_dfs = time.time()
pencarianDfs = root.Dfs_search("Log Tambah")
selesaicari_dfs = time.time()
waktucari_dfs = selesaicari_dfs - mulaicari_dfs
print(f"data ditemukan via DFS: {pencarianDfs.name if pencarianDfs else 'Tidak Ditemukan'}")
print(f"waktu yang dibutuhkan untuk DFS search adalah: {waktucari_dfs * 1000:.3f}")


mulaicari_bfs = time.time()
pencarianBfs = root.Bfs_search("Log Tambah")
selesaicari_bfs = time.time()
waktucari_bfs = selesaicari_bfs - mulaicari_bfs
print(f"data ditemukan via BFS: {pencarianBfs.name if pencarianBfs else 'Tidak Ditemukan'}")
print(f"waktu yang dibutuhkan untuk BFS search adalah: {waktucari_bfs * 1000:.3f}")
