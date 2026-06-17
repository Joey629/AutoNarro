---
id: 'Panel'
section: components
cssPrefix: pf-v6-c-panel
---import './Panel.css'

## Examples

### Basic

```html
<div class="pf-v6-c-panel">
  <div class="pf-v6-c-panel__main">
    <div class="pf-v6-c-panel__main-body">Main content</div>
  </div>
</div>

```

### Secondary

```html
<div class="pf-v6-c-panel pf-m-secondary">
  <div class="pf-v6-c-panel__main">
    <div class="pf-v6-c-panel__main-body">Main content with secondary styling</div>
  </div>
</div>

```

### Header

```html
<div class="pf-v6-c-panel">
  <div class="pf-v6-c-panel__header">Header content</div>
  <hr class="pf-v6-c-divider" />
  <div class="pf-v6-c-panel__main">
    <div class="pf-v6-c-panel__main-body">Main content</div>
  </div>
</div>

```

### Footer

```html
<div class="pf-v6-c-panel">
  <div class="pf-v6-c-panel__main">
    <div class="pf-v6-c-panel__main-body">Main content</div>
  </div>
  <div class="pf-v6-c-panel__footer">Footer content</div>
</div>

```

### Header and footer

```html
<div class="pf-v6-c-panel">
  <div class="pf-v6-c-panel__header">Header content</div>
  <hr class="pf-v6-c-divider" />
  <div class="pf-v6-c-panel__main">
    <div class="pf-v6-c-panel__main-body">Main content</div>
  </div>
  <div class="pf-v6-c-panel__footer">Footer content</div>
</div>

```

### No body

```html
<div class="pf-v6-c-panel">
  <div class="pf-v6-c-panel__main">Main content</div>
</div>

```

### Raised

```html
<div class="pf-v6-c-panel pf-m-raised">
  <div class="pf-v6-c-panel__main">
    <div class="pf-v6-c-panel__main-body">Main content</div>
  </div>
</div>

```

### Bordered

```html
<div class="pf-v6-c-panel pf-m-bordered">
  <div class="pf-v6-c-panel__main">
    <div class="pf-v6-c-panel__main-body">Main content</div>
  </div>
</div>

```

### Scrollable

```html
<div class="pf-v6-c-panel pf-m-scrollable">
  <div class="pf-v6-c-panel__main" tabindex="0">
    <div class="pf-v6-c-panel__main-body">
      Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
    </div>
  </div>
</div>

```

### Scrollable with auto height

```html
<div class="pf-v6-c-panel pf-m-scrollable-auto-height pf-m-scrollable">
  <div class="pf-v6-c-panel__main" tabindex="0">
    <div class="pf-v6-c-panel__main-body">
      Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
    </div>
  </div>
</div>

```

### Scrollable with header and footer

```html
<div class="pf-v6-c-panel pf-m-scrollable">
  <div class="pf-v6-c-panel__header">Header content</div>
  <hr class="pf-v6-c-divider" />
  <div class="pf-v6-c-panel__main" tabindex="0">
    <div class="pf-v6-c-panel__main-body">
      Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
      <br />
      <br />Main content
    </div>
  </div>
  <div class="pf-v6-c-panel__footer">Footer content</div>
</div>

```

### Pill

```html
<div class="pf-v6-c-panel pf-m-pill">
  <div class="pf-v6-c-panel__main">
    <div class="pf-v6-c-panel__main-body">Main content</div>
  </div>
</div>

```

## Documentation

### Usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-panel` | `<div>` | Initiates the panel. **Required** |
| `.pf-v6-c-panel__header` | `<div>` | Initiates the panel header. |
| `.pf-v6-c-panel__main` | `<div>` | Initiates the panel main content. |
| `.pf-v6-c-panel__main-body` | `<div>` | Initiates a panel content body container. |
| `.pf-v6-c-panel__menu` | `<div>` | Initiates a panel menu container. |
| `.pf-v6-c-panel__footer` | `<div>` | Initiates the panel footer. |
| `.pf-m-bordered` | `.pf-v6-c-panel` | Adds a border to the panel. |
| `.pf-m-no-border` | `.pf-v6-c-panel` | Removes the border from a variant that has a default border. |
| `.pf-m-raised` | `.pf-v6-c-panel` | Applies elevated styles for use when the panel appears on top of other elements. |
| `.pf-m-scrollable` | `.pf-v6-c-panel` | Modifies the panel so the main content is scrollable. |
| `.pf-m-scrollable-auto-height` | `.pf-v6-c-panel` | Modifies the panel to have an auto height when scrollable. |
| `.pf-m-secondary` | `.pf-v6-c-panel` | Modifies the panel for secondary styles. |
| `.pf-m-pill` | `.pf-v6-c-panel` | Modifies the panel for pill border radius. |
| `.pf-m-full-height` | `.pf-v6-c-panel` | Makes the panel fill the available height. |
| `.pf-m-glass` | `.pf-v6-c-panel` | Applies glass styling to the panel in glass theme. |
