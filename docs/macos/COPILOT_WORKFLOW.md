# Copilot Agent'larla Geliştirme Rehberi

## 🤖 Copilot Agent'ları Nedir?

Copilot CLI içinde farklı uzmanlık alanlarına sahip özel agent'lar bulunur. Her agent belirli görevler için optimize edilmiştir ve sizi kod yazmaktan çok **proje yönetimi** rolüne taşır.

## 📚 Mevcut Agent Türleri

### 1. **explore** - Kod Keşif Agent'ı (Haiku - Hızlı)
**Ne zaman kullanılır:**
- Kod tabanını anlamak için
- Belirli dosyaları bulmak için
- Kod yapısını sorgulamak için

**Örnekler:**
```bash
# Projedeki tüm Python dosyalarını bul
@explore "system klasöründeki tüm Python dosyalarını listele"

# Emulator yapılandırmasını anla
@explore "RetroArch yapılandırması nasıl çalışıyor?"

# macOS spesifik kodları bul
@explore "macOS ile ilgili tüm fonksiyonları göster"
```

**Özellikler:**
- ✅ Hızlı sonuç (Haiku model)
- ✅ Paralel çalıştırılabilir
- ✅ 300 kelime altında özet cevaplar

---

### 2. **task** - Komut Yürütme Agent'ı (Haiku - Hızlı)
**Ne zaman kullanılır:**
- Test, build, lint çalıştırmak için
- Bağımlılık yüklemek için
- Başarı/başarısızlık raporu almak için

**Örnekler:**
```bash
# Testleri çalıştır
@task "Tüm testleri çalıştır ve sonucu raporla"

# Bağımlılıkları yükle
@task "Python bağımlılıklarını requirements.txt'den yükle"

# Kod kalitesi kontrolü
@task "ShellCheck ile tüm bash scriptlerini kontrol et"
```

**Özellikler:**
- ✅ Başarılı komutlarda kısa özet
- ✅ Hatada tam çıktı
- ✅ Ana context'i temiz tutar

---

### 3. **general-purpose** - Genel Amaçlı Agent (Sonnet - Güçlü)
**Ne zaman kullanılır:**
- Karmaşık çok adımlı işler için
- Yeni özellik geliştirme için
- Refactoring için

**Örnekler:**
```bash
# macOS launcher geliştir
@general-purpose "macOS için emulator launcher sistemi geliştir"

# Yapılandırma sistemi oluştur
@general-purpose "YAML tabanlı emulator yapılandırma sistemi oluştur"

# Hata ayıklama ve düzeltme
@general-purpose "RetroArch başlatma hatası var, bul ve düzelt"
```

**Özellikler:**
- ✅ Tam araç seti erişimi
- ✅ Yüksek kaliteli akıl yürütme (Sonnet)
- ✅ Ayrı context'te çalışır

---

### 4. **code-review** - Kod İnceleme Agent'ı
**Ne zaman kullanılır:**
- PR öncesi kod incelemesi için
- Güvenlik açıklarını bulmak için
- Kritik hataları tespit için

**Örnekler:**
```bash
# Staged değişiklikleri incele
@code-review "Staged değişiklikleri incele"

# Branch diff incelemesi
@code-review "feat/macos-launcher branch'ini main ile karşılaştır"

# Güvenlik incelemesi
@code-review "Güvenlik açıklarını ve mantık hatalarını bul"
```

**Özellikler:**
- ✅ Sadece kritik sorunları bildirir
- ✅ Stil veya format yorumu YAPMAZ
- ✅ Kod değiştirmez, sadece raporlar

---

## 🎯 Agent Seçim Kılavuzu

```
┌─────────────────────────────────────────────────────────────┐
│ Görev Türü              │ Agent          │ Örnek           │
├─────────────────────────────────────────────────────────────┤
│ Dosya bul               │ explore        │ "*.py bul"      │
│ Kod anla                │ explore        │ "nasıl çalışır?"│
│ Test çalıştır           │ task           │ "pytest run"    │
│ Özellik geliştir        │ general-purpose│ "launcher yap"  │
│ Kod incele              │ code-review    │ "PR'ı incele"   │
│ Refactor yap            │ general-purpose│ "refactor et"   │
│ Hata düzelt             │ general-purpose│ "bug fix"       │
└─────────────────────────────────────────────────────────────┘
```

---

## 💡 Best Practices

### ✅ DOĞRU Kullanım

**1. Paralel Agent Çalıştırma**
```bash
# Aynı anda birden fazla sorgu
@explore "RetroArch yapısını açıkla" ve @explore "Python dosyalarını listele"
```

**2. Açık ve Spesifik Talimatlar**
```bash
# ✅ İyi
@general-purpose "macOS için emulator launcher geliştir: 
- Emulator path kontrolü
- Process yönetimi  
- Hata loglama"

# ❌ Kötü
@general-purpose "launcher yap"
```

**3. Doğru Agent Seçimi**
```bash
# ✅ Hızlı keşif için explore kullan
@explore "Hangi dosyalarda emulator yapılandırması var?"

# ❌ explore'a kod yazma görevi verme
@explore "Benim için bir launcher kodu yaz" # YANLIŞ!
```

---

### ❌ YANLIŞ Kullanım

**1. Agent'a Sadece Tavsiye İsteme**
```bash
# ❌ Kötü
@general-purpose "launcher nasıl yapılır tavsiye ver"

# ✅ İyi
@general-purpose "launcher'ı yap ve test et"
```

**2. Tek Dosya Okuma İçin Agent Kullanma**
```bash
# ❌ Gereksiz
@explore "README.md'yi oku"

# ✅ Doğrudan view komutu kullan
```

**3. Basit Shell Komutları İçin Task Agent**
```bash
# ❌ Gereksiz
@task "ls -la çalıştır"

# ✅ Doğrudan bash kullan
```

---

## 🔄 Geliştirme İş Akışı

### Örnek: macOS Launcher Geliştirme

**1. Keşif Aşaması**
```bash
@explore "Mevcut Windows launcher kodu nerede?"
@explore "RetroArch başlatma mekanizması nasıl çalışıyor?"
```

**2. Plan Oluşturma**
```bash
[[PLAN]] macOS için emulator launcher sistemi geliştir
```

**3. Geliştirme**
```bash
@general-purpose "Plan.md'yi oku ve macOS launcher'ı geliştir:
- system/launchers/macos/ klasörü oluştur
- Python launcher modülü yaz
- RetroArch integration ekle
- Error handling ekle"
```

**4. Test**
```bash
@task "pytest ile launcher testlerini çalıştır"
```

**5. İnceleme**
```bash
@code-review "launcher kodunu incele"
```

**6. Commit**
```bash
git add system/launchers/macos/
git commit -m "feat(macos): add emulator launcher"
```

---

## 📋 Plan Mode (Önemli!)

Karmaşık işler için **[[PLAN]]** prefix kullan:

```bash
[[PLAN]] macOS emulator launcher sistemi geliştir
```

**Plan Mode ne yapar:**
1. Gereksinimleri netleştirir (soru sorar)
2. Kod tabanını analiz eder
3. Yapılandırılmış plan oluşturur
4. `~/.copilot/session-state/<id>/plan.md` dosyasına kaydeder

**Plan başlat:**
```bash
[[PLAN]] feature açıklaması
```

**Planı uygula:**
```bash
"Planı uygula" veya "start" veya "get to work"
```

---

## 🎪 Pratik Senaryolar

### Senaryo 1: Yeni Özellik Ekleme
```bash
# 1. Önce araştır
@explore "Mevcut emulator sistemleri nasıl yapılandırılmış?"

# 2. Plan oluştur
[[PLAN]] macOS RetroArch entegrasyonu ekle

# 3. Geliştir
@general-purpose "plan.md'deki RetroArch entegrasyonunu uygula"

# 4. Test et
@task "pytest tests/macos/test_retroarch.py"

# 5. İncele
@code-review "RetroArch entegrasyon kodunu incele"
```

### Senaryo 2: Bug Fix
```bash
# 1. Problemi anla
@explore "Launcher hatası hangi dosyada oluşuyor?"

# 2. Hata ayıkla
@general-purpose "Launcher'daki memory leak sorununu bul ve düzelt"

# 3. Test et
@task "Launcher testlerini çalıştır"
```

### Senaryo 3: Refactoring
```bash
# 1. Mevcut yapıyı anla
@explore "Config sistem kodları nerede?"

# 2. Refactor planı
[[PLAN]] Config sistemini YAML tabanlı yap

# 3. Uygula
@general-purpose "Config sistemini refactor et (plan.md'ye göre)"
```

---

## 🚀 İleri Seviye İpuçları

### Model Override
Farklı model kullanmak için:
```bash
# Opus ile daha kaliteli kod
@general-purpose --model claude-opus-4.6 "karmaşık algoritma geliştir"

# Haiku ile hızlı işlem
@task --model claude-haiku-4.5 "basit test çalıştır"
```

### Context Yönetimi
- Agent'lar ayrı context'te çalışır (temiz context)
- Agent başarılı olursa sonuca güven
- Başarısız olursa prompt'u iyileştir ve tekrar dene

### Paralel Çalışma
```bash
# Aynı anda 3 explore agent
@explore "Python dosyaları" + @explore "Shell scriptleri" + @explore "Config dosyaları"
```

---

## 📖 Özet

**Siz artık bir yöneticisiniz, kodcu değil!**

1. **explore** - Bilgi topla
2. **task** - Test/build çalıştır
3. **general-purpose** - Geliştir
4. **code-review** - İncele

Her agent'a **görevini yap** de, **nasıl yapayım** deme!

---

## 🎯 Sonraki Adımlar

1. Basit bir explore ile başla:
   ```bash
   @explore "Bu projede hangi sistemler var?"
   ```

2. Bir özellik geliştir:
   ```bash
   [[PLAN]] macOS için basit bir launcher yap
   ```

3. Agent'ların sonuçlarını incele ve öğren!

---

**Unutma:** Agent'lar senin ekibin, onları akıllıca yönet! 🚀
