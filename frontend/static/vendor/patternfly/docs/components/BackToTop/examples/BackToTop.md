---
id: 'Back to top'
section: components
cssPrefix: pf-v6-c-back-to-top
---import './BackToTop.css'

## Examples

### Basic

```html
<div class="pf-v6-c-back-to-top">
  <a class="pf-v6-c-button pf-m-primary" href="#">
    <span class="pf-v6-c-button__text">Back to top</span>
    <span class="pf-v6-c-button__icon pf-m-end">
      <svg
        class="pf-v6-svg"
        viewBox="0 0 320 512"
        fill="currentColor"
        aria-hidden="true"
        role="img"
        width="1em"
        height="1em"
      >
        <path
          d="M177 159.7l136 136c9.4 9.4 9.4 24.6 0 33.9l-22.6 22.6c-9.4 9.4-24.6 9.4-33.9 0L160 255.9l-96.4 96.4c-9.4 9.4-24.6 9.4-33.9 0L7 329.7c-9.4-9.4-9.4-24.6 0-33.9l136-136c9.4-9.5 24.6-9.5 34-.1z"
        />
      </svg>
    </span>
  </a>
</div>

```

## Documentation

### Usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-back-to-top` | `<div>` | Initiates the back to top component. **Required** |
| `.pf-m-hidden` | `.pf-v6-c-back-to-top` | Modifies the component to be hidden. |
