# NotebookLM Video Export Workflow

**Pattern**: Private notebooks → Public MP4 videos in GitHub repo

## Why This Approach?

✅ **Keeps notebooks private** - Only exported MP4s are public
✅ **Self-contained** - No external video hosting dependencies
✅ **Reliable** - Thumbnail → MP4 link pattern works everywhere on GitHub
✅ **Version controlled** - Videos tracked with your code

## Workflow

### 1. Generate Video in NotebookLM

```
Open notebook → Studio panel → Create Video Overview
- Choose format: Explainer, Brief, or Overview
- Set duration (shorter = smaller file size)
- Generate video
```

### 2. Export MP4

```
Studio → Video Overview → Download (three-dot menu)
- Download as MP4
- Note the video title/description
```

### 3. Optimize (Optional)

If file size > 5 MB, recompress:

```bash
ffmpeg -i input.mp4 \
  -vf "scale=1280:720" \
  -vcodec libx264 \
  -crf 28 \
  -preset medium \
  output.mp4
```

### 4. Add to Repository

```bash
# Place in proper directory
cp output.mp4 P:/packages/your-repo/assets/video/video-name.mp4

# Create thumbnail (extract frame at 2 seconds)
ffmpeg -i output.mp4 \
  -ss 00:00:02 \
  -vframes 1 \
  -vf "scale=1280:720" \
  P:/packages/your-repo/assets/img/video-name-thumb.png

# Commit
cd P:/packages/your-repo
git add assets/video/video-name.mp4 assets/img/video-name-thumb.png
git commit -m "docs: add video overview"
git push
```

### 5. Update README

Use the template in `templates/video-section-template.md`:

```markdown
- [![Video title](assets/img/video-name-thumb.png)](https://raw.githubusercontent.com/YOUR_USER/YOUR_REPO/main/assets/video/video-name.mp4 "Video title")
```

## Directory Structure

```
your-repo/
├── assets/
│   ├── video/
│   │   ├── overview.mp4
│   │   ├── feature-tour.mp4
│   │   └── setup.mp4
│   └── img/
│       ├── overview-thumb.png
│       ├── feature-tour-thumb.png
│       └── setup-thumb.png
└── README.md
```

## Best Practices

### Video Length
- **Ideal**: 30-60 seconds for overviews
- **Maximum**: 2-3 minutes for detailed tours
- **Keep it concise** - Large files slow down clones

### Resolution
- **720p (1280×720)** - Good balance of quality and file size
- **1080p** - Only if high detail is needed
- **Avoid** 4K - Too large for GitHub repos

### File Size
- **Target**: < 5 MB per video
- **Maximum**: 10 MB (consider external hosting)
- **Optimize**: Use ffmpeg CRF 28 for good compression

### Thumbnail
- **Extract frame** from video (consistent visual)
- **16:9 aspect ratio** (1280×720 or similar)
- **Descriptive filename** (easily identify which video)

### Privacy
- ❌ **Never** share NotebookLM URLs (exposes notebook)
- ✅ **Always** use exported MP4s
- ✅ **Keep** source notebooks private

## Troubleshooting

### Video Not Playing
- Check MP4 is valid: `ffmpeg -v error -i video.mp4 -f null -`
- Verify file was committed: `git ls-files assets/video/`
- Test URL: Open raw.githubusercontent.com link in browser

### Thumbnail Not Showing
- Verify path: `assets/img/video-thumb.png`
- Check file was committed: `git ls-files assets/img/`
- Test image URL in browser

### File Too Large
- Recompress with ffmpeg (see step 3)
- Consider splitting into multiple shorter videos
- Use external hosting (YouTube, Vimeo) with thumbnail link

## Template Copy-Paste

For quick setup, copy from `templates/video-section-template.md` and customize:

```bash
# In your repo directory
cp P:/packages/github-ready/templates/video-section-template.md \
   P:/packages/your-repo/VIDEO_SECTION.md

# Edit VIDEO_SECTION.md with your specific videos
# Then copy the relevant section into your README.md
```

## References

- NotebookLM Video Overviews: https://support.google.com/notebooklm/answer/16454555
- GitHub README video best practices: https://www.govideolink.com/blog/embed-video-github-readme
- ffmpeg compression guide: https://trac.ffmpeg.org/wiki/Encode/H.264
