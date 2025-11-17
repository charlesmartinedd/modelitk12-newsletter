# Newsletter Automation Scripts

**Status**: ✅ Blogger Publishing Ready
**Last Updated**: November 17, 2025

---

## 📂 Script Inventory

### Core Scripts

Located in `/workspace/scripts/`:

1. **`publish_modelit_to_blogger.py`**
   - End-to-end newsletter processing
   - Markdown → HTML conversion
   - Image integration
   - Blogger payload generation

2. **`create_blogger_scenario_api.py`**
   - Make.com scenario creation (API)
   - Webhook setup automation
   - Payload generation

3. **`api-helpers/imgbb_helper.py`**
   - Image upload to imgbb CDN
   - Permanent URL generation
   - Multiple input formats supported

---

## 🚀 Quick Start

### Publish Week 1 to Blogger

**Prerequisites**:
- Make.com account with Blogger connected
- Webhook scenario set up (see `BLOGGER_AUTOMATION_COMPLETE.md`)

**Command**:
```bash
# From workspace root
python3 scripts/publish_modelit_to_blogger.py
```

**Output**:
- Blog data JSON
- HTML preview
- Webhook trigger payload

---

## 📊 Generated Files

All files output to `/workspace/`:

- `week1_blog_data.json` - Structured blog metadata
- `week1_blogger_content.html` - Ready-to-publish HTML
- `week1_blog_preview.html` - Browser preview
- `week1_makecom_trigger.json` - Webhook payload

---

## 🔄 Workflow

```
1. Run: publish_modelit_to_blogger.py
   ↓
2. Review: week1_blog_preview.html
   ↓
3. Trigger: Make.com webhook with payload
   ↓
4. Published: Live on Blogger
```

---

## 📝 Notes

- All scripts maintain **NO API keys** in code
- Environment variables loaded from `/root/.env`
- GitHub-safe (credentials excluded)
- Production-ready and tested

---

See `BLOGGER_AUTOMATION_COMPLETE.md` for full documentation.
