import sqlite3

# انشاء قاعدة بيانات جديدة او الاتصال بالقاعدة القائمة
conn = sqlite3.connect('accounts.db')

# إنشاء جدول accounts
conn.execute('''CREATE TABLE IF NOT EXISTS accounts
         (ID INTEGER PRIMARY KEY AUTOINCREMENT,
         username TEXT NOT NULL,
         email TEXT NOT NULL,
         password TEXT NOT NULL);''')

# إدخال بيانات مسؤول
conn.execute("INSERT INTO accounts (username, email, password) VALUES ('admin', 'admin@admin.com', '123')")

# حفظ التغييرات
conn.commit()

# إغلاق الاتصال بقاعدة البيانات
conn.close()
