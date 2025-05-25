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

# === CABANG 1: Account (Level: 1–7) ===
account = Mytree("Account")
profile = Mytree("Profile")
edit_profile = Mytree("Edit Profile")
edit_name = Mytree("Edit Name")
confirm_name = Mytree("Confirm Name")
save_name = Mytree("Save Name")
name_log = Mytree("Log Name Change")

root.addChild(account)
account.addChild(profile)
profile.addChild(edit_profile)
edit_profile.addChild(edit_name)
edit_name.addChild(confirm_name)
confirm_name.addChild(save_name)
save_name.addChild(name_log)

# Tambahan sub untuk Account (8 nodes)
security = Mytree("Security")
change_pass = Mytree("Change Password")
input_old = Mytree("Old Password")
input_new = Mytree("New Password")
confirm_new = Mytree("Confirm Password")
save_pass = Mytree("Save Password")
pass_log = Mytree("Password History")

account.addChild(security)
security.addChild(change_pass)
change_pass.addChild(input_old)
change_pass.addChild(input_new)
input_new.addChild(confirm_new)
confirm_new.addChild(save_pass)
save_pass.addChild(pass_log)

# === CABANG 2: Setting (13 nodes)
setting = Mytree("Setting")
display = Mytree("Display")
theme = Mytree("Theme")
dark = Mytree("Dark Mode")
light = Mytree("Light Mode")
font = Mytree("Font")
font_size = Mytree("Font Size")
font_style = Mytree("Font Style")
notif = Mytree("Notification")
email = Mytree("Email Notif")
sms = Mytree("SMS Notif")
push = Mytree("Push Notif")
vibration = Mytree("Vibration Setting")

root.addChild(setting)
setting.addChild(display)
display.addChild(theme)
theme.addChild(dark)
theme.addChild(light)
display.addChild(font)
font.addChild(font_size)
font.addChild(font_style)
setting.addChild(notif)
notif.addChild(email)
notif.addChild(sms)
notif.addChild(push)
push.addChild(vibration)

# === CABANG 3: Dashboard (13 nodes)
dashboard = Mytree("Dashboard")
tambah = Mytree("Tambah Data")
manual = Mytree("Manual Entry")
import_excel = Mytree("Import Excel")
validasi = Mytree("Validasi Form")
simpan = Mytree("Simpan")
log_simpan = Mytree("Log Simpan")
lihat = Mytree("Lihat Data")
table = Mytree("Table View")
map = Mytree("Map View")
statistik = Mytree("Statistik")
grafik = Mytree("Grafik")
export = Mytree("Export CSV")

root.addChild(dashboard)
dashboard.addChild(tambah)
tambah.addChild(manual)
manual.addChild(validasi)
validasi.addChild(simpan)
simpan.addChild(log_simpan)
tambah.addChild(import_excel)
dashboard.addChild(lihat)
lihat.addChild(table)
lihat.addChild(map)
dashboard.addChild(statistik)
dashboard.addChild(grafik)
dashboard.addChild(export)

# === CABANG 4: Help (7 nodes)
help = Mytree("Help")
faq = Mytree("FAQ")
contact = Mytree("Contact Us")
feedback = Mytree("Feedback")
bug = Mytree("Report Bug")
guide = Mytree("User Guide")
terms = Mytree("Terms & Conditions")

root.addChild(help)
help.addChild(faq)
help.addChild(contact)
help.addChild(feedback)
feedback.addChild(bug)
help.addChild(guide)
help.addChild(terms)

# === CABANG 5: Report (7 nodes)
report = Mytree("Report")
daily = Mytree("Daily")
weekly = Mytree("Weekly")
monthly = Mytree("Monthly")
yearly = Mytree("Yearly")
custom = Mytree("Custom Filter")
export_pdf = Mytree("Export to PDF")

root.addChild(report)
report.addChild(daily)
report.addChild(weekly)
report.addChild(monthly)
report.addChild(yearly)
report.addChild(custom)
custom.addChild(export_pdf)

# === CABANG 6: Advanced Settings (10 nodes)
advanced = Mytree("Advanced Settings")
dev_mode = Mytree("Developer Mode")
api = Mytree("API Keys")
regenerate = Mytree("Regenerate")
rate_limit = Mytree("Rate Limiting")
security_adv = Mytree("Advanced Security")
encryption = Mytree("Encryption")
audit_log = Mytree("Audit Logs")
system_log = Mytree("System Logs")
backup = Mytree("Backup")
restore = Mytree("Restore")

root.addChild(advanced)
advanced.addChild(dev_mode)
advanced.addChild(api)
api.addChild(regenerate)
api.addChild(rate_limit)
advanced.addChild(security_adv)
security_adv.addChild(encryption)
advanced.addChild(audit_log)
audit_log.addChild(system_log)
audit_log.addChild(backup)
backup.addChild(restore)


print(root.showTree())

mulaicari_dfs = time.time()
pencarianDfs = root.Dfs_search("API Keys")
selesaicari_dfs = time.time()
waktucari_dfs = selesaicari_dfs - mulaicari_dfs
print(f"data ditemukan via DFS: {pencarianDfs.name if pencarianDfs else 'Tidak Ditemukan'}")
print(f"waktu yang dibutuhkan untuk DFS search adalah: {waktucari_dfs * 1000:.3f}")


mulaicari_bfs = time.time()
pencarianBfs = root.Bfs_search("API Keys")
selesaicari_bfs = time.time()
waktucari_bfs = selesaicari_bfs - mulaicari_bfs
print(f"data ditemukan via BFS: {pencarianBfs.name if pencarianBfs else 'Tidak Ditemukan'}")
print(f"waktu yang dibutuhkan untuk BFS search adalah: {waktucari_bfs * 1000:.3f}")
