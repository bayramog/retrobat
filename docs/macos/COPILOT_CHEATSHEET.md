# Copilot Agent Cheatsheet 🚀

## Hızlı Başvuru

### Agent Çağırma Syntax
```bash
@<agent-type> "görev açıklaması"
@<agent-type> --model <model-name> "görev"
```

---

## 🔍 EXPLORE Agent (Keşif)

### Dosya Bulma
```bash
@explore "tüm Python dosyalarını bul"
@explore "system klasöründeki .sh uzantılı dosyalar"
@explore "emulator ile ilgili tüm dosyalar"
```

### Kod Anlama
```bash
@explore "RetroArch nasıl başlatılıyor?"
@explore "build.ini dosyası ne işe yarıyor?"
@explore "launcher mantığı nasıl çalışıyor?"
```

### Yapı Analizi
```bash
@explore "projedeki tüm modülleri listele"
@explore "test yapısı nasıl organize edilmiş?"
@explore "hangi bağımlılıklar kullanılıyor?"
```

---

## ⚙️ TASK Agent (Komut Yürütme)

### Test
```bash
@task "tüm testleri çalıştır"
@task "pytest tests/macos/"
@task "specific test dosyasını çalıştır: test_launcher.py"
```

### Build & Lint
```bash
@task "projeyi build et"
@task "ShellCheck ile bash scriptleri kontrol et"
@task "Python kodunu pylint ile kontrol et"
```

### Bağımlılık Yönetimi
```bash
@task "pip install -r requirements.txt"
@task "npm install"
@task "bağımlılıkları güncelle"
```

---

## 🛠️ GENERAL-PURPOSE Agent (Genel Geliştirme)

### Özellik Geliştirme
```bash
@general-purpose "macOS için emulator launcher sistemi geliştir"
@general-purpose "YAML yapılandırma parser ekle"
@general-purpose "logging sistemi kur"
```

### Refactoring
```bash
@general-purpose "config sistemini YAML tabanlı yap"
@general-purpose "launcher kodunu modülerleştir"
@general-purpose "error handling'i iyileştir"
```

### Bug Fix
```bash
@general-purpose "memory leak'i bul ve düzelt"
@general-purpose "launcher çalışmıyor, hata ayıkla"
@general-purpose "test başarısız oluyor, düzelt"
```

---

## 🔍 CODE-REVIEW Agent (İnceleme)

### Değişiklik İncelemesi
```bash
@code-review "staged değişiklikleri incele"
@code-review "son commit'i incele"
@code-review "feat/macos-launcher branch'ini incele"
```

### Güvenlik İncelemesi
```bash
@code-review "güvenlik açıklarını bul"
@code-review "shell injection riskleri var mı?"
@code-review "input validation eksiklikleri"
```

---

## 📋 PLAN Mode

### Plan Oluşturma
```bash
[[PLAN]] macOS emulator launcher sistemi
[[PLAN]] test framework kurulumu
[[PLAN]] CI/CD pipeline oluştur
```

### Plan Uygulama
```bash
"planı uygula"
"start"
"get to work"
"implement it"
```

---

## 🎯 Gerçek Dünya Örnekleri

### Örnek 1: Yeni Module Ekleme
```bash
# 1. Araştır
@explore "mevcut launcher modülleri nasıl organize edilmiş?"

# 2. Plan yap
[[PLAN]] macOS için RetroArch launcher modülü ekle

# 3. Geliştir
@general-purpose "plan.md'deki RetroArch launcher'ı geliştir"

# 4. Test et
@task "pytest tests/macos/test_retroarch_launcher.py -v"

# 5. İncele
@code-review "RetroArch launcher kodunu incele"
```

### Örnek 2: Configuration Sistemi
```bash
# YAML config için gerekli yapıyı anla
@explore "mevcut configuration nasıl yönetiliyor?"

# Config sistemi geliştir
@general-purpose "YAML tabanlı emulator configuration sistemi geliştir:
- YAML parser
- Config validation
- Default values
- Error handling
Dosya: system/config/emulator_config.py"

# Test et
@task "pytest tests/config/test_emulator_config.py"
```

### Örnek 3: Hata Ayıklama
```bash
# Hatayı bul
@explore "launcher hatası hangi dosyada?"

# Log çıktısını analiz et
@general-purpose "launcher.log dosyasını analiz et ve hatanın kaynağını bul"

# Düzelt
@general-purpose "bulunan hatayı düzelt ve test ekle"

# Doğrula
@task "launcher'ı test et"
```

---

## 💡 Pro Tips

### Paralel Agent Kullanımı
```bash
# Aynı anda birden fazla explore
@explore "Python modules" @explore "Shell scripts" @explore "Config files"
```

### Model Override
```bash
# Daha güçlü model ile karmaşık görev
@general-purpose --model claude-opus-4.6 "karmaşık algoritma optimizasyonu"

# Hızlı model ile basit görev
@task --model claude-haiku-4.5 "basit test run"
```

### Chain of Agents
```bash
# 1. Keşfet
@explore "authentication sistemi nerede?"

# Sonucu bekle, sonra:
# 2. Geliştir
@general-purpose "bulunan auth sistemine macOS keychain entegrasyonu ekle"

# 3. Test et
@task "auth testlerini çalıştır"

# 4. İncele
@code-review "auth değişikliklerini incele"
```

---

## ❌ Yaygın Hatalar

### YANLIŞ ❌
```bash
@explore "benim için launcher kodu yaz"  # explore geliştirme yapmaz!
@task "bana testleri açıkla"  # task açıklama yapmaz, çalıştırır!
@general-purpose "nasıl yapmalıyım?"  # tavsiye değil, uygulama iste!
```

### DOĞRU ✅
```bash
@explore "launcher kodu nerede?"
@task "testleri çalıştır ve sonucu raporla"
@general-purpose "launcher'ı geliştir ve test et"
```

---

## 🎪 Workflow Templates

### Template: Feature Development
```bash
# Phase 1: Research
@explore "mevcut <feature> implementasyonu"
@explore "ilgili dependencies neler?"

# Phase 2: Plan
[[PLAN]] <feature> ekle

# Phase 3: Implement
@general-purpose "plan.md'deki <feature>'ı uygula"

# Phase 4: Test
@task "<feature> testlerini çalıştır"

# Phase 5: Review
@code-review "<feature> kodunu incele"

# Phase 6: Commit
git add <files>
git commit -m "feat(scope): add <feature>"
```

### Template: Bug Fix
```bash
# Phase 1: Identify
@explore "<bug> nerede oluşuyor?"

# Phase 2: Fix
@general-purpose "<bug>'ı bul ve düzelt"

# Phase 3: Test
@task "regression testlerini çalıştır"

# Phase 4: Commit
git commit -m "fix(scope): resolve <bug>"
```

### Template: Refactoring
```bash
# Phase 1: Understand
@explore "mevcut <component> yapısı"

# Phase 2: Plan
[[PLAN]] <component> refactor

# Phase 3: Refactor
@general-purpose "plan.md'deki refactoring'i uygula"

# Phase 4: Validate
@task "tüm testleri çalıştır"
@code-review "refactoring değişikliklerini incele"
```

---

## 🚀 Hızlı Komutlar

```bash
# Session yönetimi
/resume                    # Session'ları listele
/session                   # Mevcut session bilgisi
/clear                     # Konuşmayı temizle

# Context yönetimi
/context                   # Token kullanımı
/compact                   # History'i özetle

# Model değiştir
/model                     # Mevcut model
/models                    # Model listesi

# Çalışma dizini
/cwd                       # Mevcut dizin
/cd <path>                 # Dizin değiştir

# Task yönetimi
/tasks                     # Arka plan görevleri

# Plan yönetimi
/plan                      # Plan oluştur
/session plan              # Mevcut planı göster

# Değişiklikleri gör
/diff                      # Git diff göster
```

---

## 📖 Kısaltmalar

- **GP** = general-purpose
- **EXP** = explore  
- **TSK** = task
- **REV** = code-review

---

**Hızlı başlamak için:**
```bash
@explore "Bu projede neler var?"
```

🎯 **Unutma:** Sen yöneticisin, agent'lar ekibin!
