---
id: 'Compass'
beta: true
section: components
cssPrefix: pf-v6-c-compass
---import './Compass.css';

## Examples

### Basic

In a basic Compass layout, the page structure is defined by the order of elements nested within `.pf-v6-c-compass__container` (inside `.pf-v6-c-compass`):

* **Header:** Content rendered at the top of the page (`.pf-v6-c-compass__header`), typically containing a logo (`.pf-v6-c-compass__logo`), middle navigation (`.pf-v6-c-compass__nav`), and profile (`.pf-v6-c-compass__profile`).
* **Start sidebar:** Content rendered at the horizontal start of the page (by default, the left side). In this example, a `.pf-v6-c-compass__sidebar` with the `.pf-m-start` modifier.
* **Main:** Content rendered in the center of the page. The `.pf-v6-c-compass__main` wrapper contains a [hero component](/components/hero), the main header (`.pf-v6-c-compass__main-header`), the content area (`.pf-v6-c-compass__content`), and the main footer (`.pf-v6-c-compass__main-footer`) with the message bar.
* **End sidebar:** Content rendered at the horizontal end of the page (by default, the right side). In this example, a `.pf-v6-c-compass__sidebar` with the `.pf-m-end` modifier.
* **Footer:** Content rendered at the bottom of the page (`.pf-v6-c-compass__footer`).

```html isBeta
<div class="pf-v6-c-compass pf-m-animate-smoothly">
  <div class="pf-v6-c-compass__container">
    <div class="pf-v6-c-compass__header pf-m-expanded">
      <div class="pf-v6-c-compass__logo">logo</div>

      <div class="pf-v6-c-compass__nav">
        <div class="pf-v6-c-compass__nav-content">
          <div class="pf-v6-c-compass__nav-home">home</div>

          <div class="pf-v6-c-compass__nav-main">main</div>

          <div class="pf-v6-c-compass__nav-search">search</div>
        </div>
      </div>
      <div class="pf-v6-c-compass__profile">profile</div>
    </div>
    <div
      class="pf-v6-c-compass__sidebar pf-m-expanded pf-m-start"
    >sidebar (start)</div>

    <div class="pf-v6-c-compass__main">
      <div class="pf-v6-c-compass__hero">hero</div>
      <div class="pf-v6-c-compass__main-header">
        <div class="pf-v6-c-compass__main-header-content">main header</div>
      </div>
      <div class="pf-v6-c-compass__content">content</div>

      <div class="pf-v6-c-compass__main-footer pf-m-expanded">
        <div class="pf-v6-c-compass__message-bar">message bar</div>
      </div>
    </div>
    <div class="pf-v6-c-compass__sidebar pf-m-expanded pf-m-end">sidebar (end)</div>

    <div class="pf-v6-c-compass__footer pf-m-expanded">footer</div>
  </div>
</div>

```

### Docked

```html isBeta
<div class="pf-v6-c-compass pf-m-animate-smoothly pf-m-docked">
  <div class="pf-v6-c-compass__container">
    <header class="pf-v6-c-masthead pf-m-display-inline">
      <div class="pf-v6-c-masthead__main">masthead main</div>
      <div class="pf-v6-c-masthead__content">masthead content</div>
    </header>
    <div class="pf-v6-c-compass__dock">
      <div class="pf-v6-c-compass__dock-main">dock</div>
    </div>
    <div class="pf-v6-c-compass__main">
      <div class="pf-v6-c-compass__main-header">
        <div class="pf-v6-c-compass__main-header-content">main header</div>
      </div>
      <div class="pf-v6-c-compass__content">content</div>
    </div>
  </div>
</div>

```

## Documentation

### Usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-compass` | `<div>` | Outermost wrapper for the Compass component. Handles background. **Required** |
| `.pf-v6-c-compass__container` | `<div>` | Grid wrapper for Compass regions. **Required** |
| `.pf-v6-c-compass__header` | `<div>` | Initiates the Compass header. **Required** |
| `.pf-v6-c-compass__logo` | `<div>` | Initiates the Compass logo header. |
| `.pf-v6-c-compass__dock` | `<div>` | Initiates the Compass dock. |
| `.pf-v6-c-compass__profile` | `<div>` | Initiates the Compass profile. |
| `.pf-v6-c-compass__dock-main` | `<div>` | Initiates the Compass dock main wrapper. |
| `.pf-v6-c-compass__sidebar` | `<div>` | Initiates a Compass sidebar. **Required** |
| `.pf-v6-c-compass__main` | `<div>` | Initiates the Compass main wrapper. **Required** |
| `.pf-v6-c-compass__main-header` | `<div>` | Initiates the Compass main header. |
| `.pf-v6-c-compass__main-header-content` | `<div>` | Initiates the Compass main header content. This should be passed into a glass panel component. |
| `.pf-v6-c-compass__main-header-title` | `<div>` | Initiates a title within the Compass main header content. |
| `.pf-v6-c-compass__main-header-toolbar` | `<div>` | Initiates a toolbar of actions within the Compass main header content. |
| `.pf-v6-c-compass__content` | `<div>` | Initiates the Compass content. **Required** |
| `.pf-v6-c-compass__main-footer` | `<div>` | Initiates the Compass main footer. **Required** |
| `.pf-v6-c-compass__nav` | `<div>` | Initiates a Compass container for site navigation. |
| `.pf-v6-c-compass__nav-content` | `<div>` | Initiates a Compass container for navigation content. |
| `.pf-v6-c-compass__nav-home` | `<div>` | Initiates a container for Compass home button. |
| `.pf-v6-c-compass__nav-main` | `<div>` | Initiates a container for Compass navigation main content. |
| `.pf-v6-c-compass__nav-search` | `<div>` | Initiates a container for Compass search button. |
| `.pf-v6-c-compass__footer` | `<div>` | Initiates the Compass footer. |
| `.pf-v6-c-compass__message-bar` | `<div>` | Initiates the Compass message bar. |
| `.pf-m-docked` | `.pf-v6-c-compass` | Modifies for dock layout. |
| `.pf-m-no-screen-warning` | `.pf-v6-c-compass` | Disables the screen warning that shows on smaller viewports. |
| `.pf-m-start` | `.pf-v6-c-compass__sidebar` | Modifies a Compass sidebar for start styles. **Required** |
| `.pf-m-end` | `.pf-v6-c-compass__sidebar` | Modifies a Compass sidebar for end styles. **Required** |
| `.pf-m-expanded` | `.pf-v6-c-compass__header`, `.pf-v6-c-compass__sidebar`, `.pf-v6-c-compass__main-footer`, `.pf-v6-c-compass__footer` | Modifies a Compass section for expanded styles. |
