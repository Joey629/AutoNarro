---
id: Popover
section: components
cssPrefix: pf-v6-c-popover
---import './Popover.css'

## Examples

### Top

```html isFullscreen
<div
  class="pf-v6-c-popover pf-m-top"
  role="dialog"
  aria-modal="true"
  aria-labelledby="popover-top-header"
  aria-describedby="popover-top-body"
>
  <div class="pf-v6-c-popover__arrow"></div>
  <div class="pf-v6-c-popover__content">
    <div class="pf-v6-c-popover__close">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Close"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
            />
          </svg>
        </span>
      </button>
    </div>
    <header class="pf-v6-c-popover__header">
      <div class="pf-v6-c-popover__title" id="popover-top-header">
        <h1 class="pf-v6-c-popover__title-text">Popover header</h1>
      </div>
    </header>
    <div
      class="pf-v6-c-popover__body"
      id="popover-top-body"
    >Popovers are triggered by click rather than hover. Click again to close.</div>
    <footer class="pf-v6-c-popover__footer">Popover footer</footer>
  </div>
</div>

```

### Right

```html isFullscreen
<div
  class="pf-v6-c-popover pf-m-right"
  role="dialog"
  aria-modal="true"
  aria-labelledby="popover-right-header"
  aria-describedby="popover-right-body"
>
  <div class="pf-v6-c-popover__arrow"></div>
  <div class="pf-v6-c-popover__content">
    <div class="pf-v6-c-popover__close">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Close"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
            />
          </svg>
        </span>
      </button>
    </div>
    <header class="pf-v6-c-popover__header">
      <div class="pf-v6-c-popover__title" id="popover-right-header">
        <h1 class="pf-v6-c-popover__title-text">Popover header</h1>
      </div>
    </header>
    <div
      class="pf-v6-c-popover__body"
      id="popover-right-body"
    >Popovers are triggered by click rather than hover. Click again to close.</div>
    <footer class="pf-v6-c-popover__footer">Popover footer</footer>
  </div>
</div>

```

### Bottom

```html isFullscreen
<div
  class="pf-v6-c-popover pf-m-bottom"
  role="dialog"
  aria-modal="true"
  aria-labelledby="popover-bottom-header"
  aria-describedby="popover-bottom-body"
>
  <div class="pf-v6-c-popover__arrow"></div>
  <div class="pf-v6-c-popover__content">
    <div class="pf-v6-c-popover__close">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Close"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
            />
          </svg>
        </span>
      </button>
    </div>
    <header class="pf-v6-c-popover__header">
      <div class="pf-v6-c-popover__title" id="popover-bottom-header">
        <h1 class="pf-v6-c-popover__title-text">Popover header</h1>
      </div>
    </header>
    <div
      class="pf-v6-c-popover__body"
      id="popover-bottom-body"
    >Popovers are triggered by click rather than hover. Click again to close.</div>
    <footer class="pf-v6-c-popover__footer">Popover footer</footer>
  </div>
</div>

```

### Left

```html isFullscreen
<div
  class="pf-v6-c-popover pf-m-left"
  role="dialog"
  aria-modal="true"
  aria-labelledby="popover-left-header"
  aria-describedby="popover-left-body"
>
  <div class="pf-v6-c-popover__arrow"></div>
  <div class="pf-v6-c-popover__content">
    <div class="pf-v6-c-popover__close">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Close"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
            />
          </svg>
        </span>
      </button>
    </div>
    <header class="pf-v6-c-popover__header">
      <div class="pf-v6-c-popover__title" id="popover-left-header">
        <h1 class="pf-v6-c-popover__title-text">Popover header</h1>
      </div>
    </header>
    <div
      class="pf-v6-c-popover__body"
      id="popover-left-body"
    >Popovers are triggered by click rather than hover. Click again to close.</div>
    <footer class="pf-v6-c-popover__footer">Popover footer</footer>
  </div>
</div>

```

### Left top

```html isFullscreen
<div
  class="pf-v6-c-popover pf-m-left-top"
  role="dialog"
  aria-modal="true"
  aria-labelledby="popover-left-start-header"
  aria-describedby="popover-left-start-body"
>
  <div class="pf-v6-c-popover__arrow"></div>
  <div class="pf-v6-c-popover__content">
    <div class="pf-v6-c-popover__close">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Close"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
            />
          </svg>
        </span>
      </button>
    </div>
    <header class="pf-v6-c-popover__header">
      <div class="pf-v6-c-popover__title" id="popover-left-start-header">
        <h1 class="pf-v6-c-popover__title-text">Popover header</h1>
      </div>
    </header>
    <div
      class="pf-v6-c-popover__body"
      id="popover-left-start-body"
    >This popover is to the left and at the start position</div>
    <footer class="pf-v6-c-popover__footer">Popover footer</footer>
  </div>
</div>

```

### Left bottom

```html isFullscreen
<div
  class="pf-v6-c-popover pf-m-left-bottom"
  role="dialog"
  aria-modal="true"
  aria-labelledby="popover-left-end-header"
  aria-describedby="popover-left-end-body"
>
  <div class="pf-v6-c-popover__arrow"></div>
  <div class="pf-v6-c-popover__content">
    <div class="pf-v6-c-popover__close">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Close"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
            />
          </svg>
        </span>
      </button>
    </div>
    <header class="pf-v6-c-popover__header">
      <div class="pf-v6-c-popover__title" id="popover-left-end-header">
        <h1 class="pf-v6-c-popover__title-text">Popover header</h1>
      </div>
    </header>
    <div
      class="pf-v6-c-popover__body"
      id="popover-left-end-body"
    >This popover is to the left and at the end position</div>
    <footer class="pf-v6-c-popover__footer">Popover footer</footer>
  </div>
</div>

```

### Bottom left

```html isFullscreen
<div
  class="pf-v6-c-popover pf-m-bottom-left"
  role="dialog"
  aria-modal="true"
  aria-labelledby="popover-bottom-start-header"
  aria-describedby="popover-bottom-start-body"
>
  <div class="pf-v6-c-popover__arrow"></div>
  <div class="pf-v6-c-popover__content">
    <div class="pf-v6-c-popover__close">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Close"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
            />
          </svg>
        </span>
      </button>
    </div>
    <header class="pf-v6-c-popover__header">
      <div class="pf-v6-c-popover__title" id="popover-bottom-start-header">
        <h1 class="pf-v6-c-popover__title-text">Popover header</h1>
      </div>
    </header>
    <div
      class="pf-v6-c-popover__body"
      id="popover-bottom-start-body"
    >This popover is to the bottom and at the start position</div>
    <footer class="pf-v6-c-popover__footer">Popover footer</footer>
  </div>
</div>

```

### Bottom right

```html isFullscreen
<div
  class="pf-v6-c-popover pf-m-bottom-right"
  role="dialog"
  aria-modal="true"
  aria-labelledby="popover-bottom-end-header"
  aria-describedby="popover-bottom-end-body"
>
  <div class="pf-v6-c-popover__arrow"></div>
  <div class="pf-v6-c-popover__content">
    <div class="pf-v6-c-popover__close">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Close"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
            />
          </svg>
        </span>
      </button>
    </div>
    <header class="pf-v6-c-popover__header">
      <div class="pf-v6-c-popover__title" id="popover-bottom-end-header">
        <h1 class="pf-v6-c-popover__title-text">Popover header</h1>
      </div>
    </header>
    <div
      class="pf-v6-c-popover__body"
      id="popover-bottom-end-body"
    >This popover is to the bottom and at the end position</div>
    <footer class="pf-v6-c-popover__footer">Popover footer</footer>
  </div>
</div>

```

### Without header/footer

```html isFullscreen
<div
  class="pf-v6-c-popover pf-m-right"
  role="dialog"
  aria-modal="true"
  aria-label="Popover with no header example"
  aria-describedby="popover-no-header-body"
>
  <div class="pf-v6-c-popover__arrow"></div>
  <div class="pf-v6-c-popover__content">
    <div class="pf-v6-c-popover__close">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Close"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
            />
          </svg>
        </span>
      </button>
    </div>
    <div
      class="pf-v6-c-popover__body"
      id="popover-no-header-body"
    >Popovers are triggered by click rather than hover. Click again to close.</div>
  </div>
</div>

```

### No padding

```html isFullscreen
<div
  class="pf-v6-c-popover pf-m-right pf-m-no-padding"
  role="dialog"
  aria-modal="true"
  aria-label="Popover with no padding example"
  aria-describedby="popover-no-padding-body"
>
  <div class="pf-v6-c-popover__arrow"></div>
  <div class="pf-v6-c-popover__content">
    <div
      class="pf-v6-c-popover__body"
      id="popover-no-padding-body"
    >This popover has no padding itself. Instead it is intended for use with content that has its own padding that prevents it from touching the popover container's edges.</div>
  </div>
</div>

```

### Width auto

```html isFullscreen
<div
  class="pf-v6-c-popover pf-m-right pf-m-width-auto"
  role="dialog"
  aria-modal="true"
  aria-labelledby="popover-width-auto-header"
  aria-describedby="popover-width-auto-body"
>
  <div class="pf-v6-c-popover__arrow"></div>
  <div class="pf-v6-c-popover__content">
    <div class="pf-v6-c-popover__close">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Close"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
            />
          </svg>
        </span>
      </button>
    </div>
    <header class="pf-v6-c-popover__header">
      <div class="pf-v6-c-popover__title" id="popover-width-auto-header">
        <h1 class="pf-v6-c-popover__title-text">Popover header</h1>
      </div>
    </header>
    <div
      class="pf-v6-c-popover__body"
      id="popover-width-auto-body"
    >Popovers body</div>
    <footer class="pf-v6-c-popover__footer">Popover footer</footer>
  </div>
</div>

```

### Popover with icon in the title

```html isFullscreen
<div
  class="pf-v6-c-popover pf-m-left"
  role="dialog"
  aria-modal="true"
  aria-labelledby="popover-icon-title-header"
  aria-describedby="popover-icon-title-body"
>
  <div class="pf-v6-c-popover__arrow"></div>
  <div class="pf-v6-c-popover__content">
    <div class="pf-v6-c-popover__close">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Close"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
            />
          </svg>
        </span>
      </button>
    </div>
    <header class="pf-v6-c-popover__header">
      <div class="pf-v6-c-popover__title" id="popover-icon-title-header">
        <span class="pf-v6-c-popover__title-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 576 512"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M576 240c0-23.63-12.95-44.04-32-55.12V32.01C544 23.26 537.02 0 512 0c-7.12 0-14.19 2.38-19.98 7.02l-85.03 68.03C364.28 109.19 310.66 128 256 128H64c-35.35 0-64 28.65-64 64v96c0 35.35 28.65 64 64 64h33.7c-1.39 10.48-2.18 21.14-2.18 32 0 39.77 9.26 77.35 25.56 110.94 5.19 10.69 16.52 17.06 28.4 17.06h74.28c26.05 0 41.69-29.84 25.9-50.56-16.4-21.52-26.15-48.36-26.15-77.44 0-11.11 1.62-21.79 4.41-32H256c54.66 0 108.28 18.81 150.98 52.95l85.03 68.03a32.023 32.023 0 0 0 19.98 7.02c24.92 0 32-22.78 32-32V295.13C563.05 284.04 576 263.63 576 240zm-96 141.42l-33.05-26.44C392.95 311.78 325.12 288 256 288v-96c69.12 0 136.95-23.78 190.95-66.98L480 98.58v282.84z"
            />
          </svg>
        </span>
        <h1 class="pf-v6-c-popover__title-text">Popover with icon title</h1>
      </div>
    </header>
    <div
      class="pf-v6-c-popover__body"
      id="popover-icon-title-body"
    >Popovers are triggered by click rather than hover. Click again to close.</div>
    <footer class="pf-v6-c-popover__footer">Popover footer</footer>
  </div>
</div>

```

### Custom alert popover

```html isFullscreen
<div
  class="pf-v6-c-popover pf-m-custom pf-m-left"
  role="dialog"
  aria-modal="true"
  aria-labelledby="popover-custom-alert-header"
  aria-describedby="popover-custom-alert-body"
>
  <div class="pf-v6-c-popover__arrow"></div>
  <div class="pf-v6-c-popover__content">
    <div class="pf-v6-c-popover__close">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Close"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
            />
          </svg>
        </span>
      </button>
    </div>
    <header class="pf-v6-c-popover__header">
      <div class="pf-v6-c-popover__title" id="popover-custom-alert-header">
        <span class="pf-v6-c-popover__title-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M28.75 22v3.5c0 .689-.561 1.25-1.25 1.25h-7.521c.005.084.021.166.021.25 0 2.206-1.794 4-4 4s-4-1.794-4-4c0-.084.016-.166.021-.25H4.5c-.689 0-1.25-.561-1.25-1.25V22a.75.75 0 0 1 .75-.75c1.24 0 2.25-1.009 2.25-2.25v-4c0-4.826 3.528-8.833 8.138-9.605A2.482 2.482 0 0 1 13.5 3.5C13.5 2.122 14.621 1 16 1s2.5 1.122 2.5 2.5c0 .761-.349 1.436-.888 1.895 4.61.772 8.138 4.779 8.138 9.605v4c0 1.241 1.01 2.25 2.25 2.25a.75.75 0 0 1 .75.75Z"
            />
          </svg>
        </span>
        <h1 class="pf-v6-c-popover__title-text">
          <span class="pf-v6-screen-reader">
            Custom
            alert:
          </span>
          Custom popover title
        </h1>
      </div>
    </header>
    <div
      class="pf-v6-c-popover__body"
      id="popover-custom-alert-body"
    >Popovers are triggered by click rather than hover. Click again to close.</div>
    <footer class="pf-v6-c-popover__footer">Popover footer</footer>
  </div>
</div>

```

### Info alert popover

```html isFullscreen
<div
  class="pf-v6-c-popover pf-m-info pf-m-top"
  role="dialog"
  aria-modal="true"
  aria-labelledby="popover-info-alert-header"
  aria-describedby="popover-info-alert-body"
>
  <div class="pf-v6-c-popover__arrow"></div>
  <div class="pf-v6-c-popover__content">
    <div class="pf-v6-c-popover__close">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Close"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
            />
          </svg>
        </span>
      </button>
    </div>
    <header class="pf-v6-c-popover__header">
      <div class="pf-v6-c-popover__title" id="popover-info-alert-header">
        <span class="pf-v6-c-popover__title-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm1.5 22a1.5 1.5 0 1 1-3 0v-5.157l-.188.04a1.5 1.5 0 0 1-.625-2.934l1.956-.416c.112-.024.223-.032.333-.03l.024-.002a1.5 1.5 0 0 1 1.5 1.5v7Zm-.08-12.58c-.38.37-.89.58-1.42.58a1.998 1.998 0 0 1-1.851-2.76c.051-.13.11-.24.19-.35.07-.11.15-.21.25-.3.74-.75 2.08-.75 2.83 0 .09.09.17.19.24.3.08.11.14.22.189.35.05.12.09.24.11.37.03.13.04.26.04.39 0 .53-.21 1.04-.58 1.42Z"
            />
          </svg>
        </span>
        <h1 class="pf-v6-c-popover__title-text">
          <span class="pf-v6-screen-reader">
            Info
            alert:
          </span>
          Info popover title
        </h1>
      </div>
    </header>
    <div
      class="pf-v6-c-popover__body"
      id="popover-info-alert-body"
    >Popovers are triggered by click rather than hover. Click again to close.</div>
    <footer class="pf-v6-c-popover__footer">Popover footer</footer>
  </div>
</div>

```

### Success alert popover

```html isFullscreen
<div
  class="pf-v6-c-popover pf-m-success pf-m-top"
  role="dialog"
  aria-modal="true"
  aria-labelledby="popover-success-alert-header"
  aria-describedby="popover-success-alert-body"
>
  <div class="pf-v6-c-popover__arrow"></div>
  <div class="pf-v6-c-popover__content">
    <div class="pf-v6-c-popover__close">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Close"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
            />
          </svg>
        </span>
      </button>
    </div>
    <header class="pf-v6-c-popover__header">
      <div class="pf-v6-c-popover__title" id="popover-success-alert-header">
        <span class="pf-v6-c-popover__title-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm7.795 11.795-8.646 8.646c-.317.317-.733.475-1.149.475s-.832-.158-1.149-.475l-4.646-4.646a1.126 1.126 0 0 1 1.591-1.591l4.205 4.205 8.205-8.205a1.126 1.126 0 0 1 1.591 1.591Z"
            />
          </svg>
        </span>
        <h1 class="pf-v6-c-popover__title-text">
          <span class="pf-v6-screen-reader">
            Success
            alert:
          </span>
          Success popover title
        </h1>
      </div>
    </header>
    <div
      class="pf-v6-c-popover__body"
      id="popover-success-alert-body"
    >Popovers are triggered by click rather than hover. Click again to close.</div>
    <footer class="pf-v6-c-popover__footer">Popover footer</footer>
  </div>
</div>

```

### Warning alert popover

```html isFullscreen
<div
  class="pf-v6-c-popover pf-m-warning pf-m-top"
  role="dialog"
  aria-modal="true"
  aria-labelledby="popover-warning-alert-header"
  aria-describedby="popover-warning-alert-body"
>
  <div class="pf-v6-c-popover__arrow"></div>
  <div class="pf-v6-c-popover__content">
    <div class="pf-v6-c-popover__close">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Close"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
            />
          </svg>
        </span>
      </button>
    </div>
    <header class="pf-v6-c-popover__header">
      <div class="pf-v6-c-popover__title" id="popover-warning-alert-header">
        <span class="pf-v6-c-popover__title-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="m31.874 28.514-15.011-27a1.001 1.001 0 0 0-1.748 0l-15.011 27A1 1 0 0 0 .978 30H31a1 1 0 0 0 .874-1.486ZM14.5 12a1.5 1.5 0 0 1 3 0v5a1.5 1.5 0 0 1-3 0v-5ZM16 26.001a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 26.001Z"
            />
          </svg>
        </span>
        <h1 class="pf-v6-c-popover__title-text">
          <span class="pf-v6-screen-reader">
            Warning
            alert:
          </span>
          Warning popover title
        </h1>
      </div>
    </header>
    <div
      class="pf-v6-c-popover__body"
      id="popover-warning-alert-body"
    >Popovers are triggered by click rather than hover. Click again to close.</div>
    <footer class="pf-v6-c-popover__footer">Popover footer</footer>
  </div>
</div>

```

### Danger alert popover

```html isFullscreen
<div
  class="pf-v6-c-popover pf-m-danger pf-m-top"
  role="dialog"
  aria-modal="true"
  aria-labelledby="popover-danger-alert-header"
  aria-describedby="popover-danger-alert-body"
>
  <div class="pf-v6-c-popover__arrow"></div>
  <div class="pf-v6-c-popover__content">
    <div class="pf-v6-c-popover__close">
      <button
        class="pf-v6-c-button pf-m-plain"
        type="button"
        aria-label="Close"
      >
        <span class="pf-v6-c-button__icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 20 20"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M17.8 16.2 11.59 10l6.21-6.21c.42-.46.39-1.17-.07-1.59-.43-.4-1.09-.4-1.52 0l-6.2 6.2-6.22-6.19c-.44-.44-1.15-.44-1.59 0-.44.44-.44 1.15 0 1.59l6.2 6.21-6.2 6.2c-.42.46-.39 1.17.07 1.59.43.4 1.09.4 1.52 0L10 11.59l6.2 6.2c.44.44 1.15.44 1.59 0 .44-.45.44-1.16 0-1.6Z"
            />
          </svg>
        </span>
      </button>
    </div>
    <header class="pf-v6-c-popover__header">
      <div class="pf-v6-c-popover__title" id="popover-danger-alert-header">
        <span class="pf-v6-c-popover__title-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 32 32"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm-1.5 8a1.5 1.5 0 1 1 3 0v7a1.5 1.5 0 1 1-3 0V9ZM16 25.001a2 2 0 1 1-.001-3.999A2 2 0 0 1 16 25.001Z"
            />
          </svg>
        </span>
        <h1 class="pf-v6-c-popover__title-text">
          <span class="pf-v6-screen-reader">
            Danger
            alert:
          </span>
          Danger popover title
        </h1>
      </div>
    </header>
    <div
      class="pf-v6-c-popover__body"
      id="popover-danger-alert-body"
    >Popovers are triggered by click rather than hover. Click again to close.</div>
    <footer class="pf-v6-c-popover__footer">Popover footer</footer>
  </div>
</div>

```

## Documentation

### Overview

A popover is used to provide contextual information for another component on click.  The popover itself is made up of two main elements: arrow and content. The content element follows the pattern of the popover box component, with a close icon in the top right corner, as well as a header and body.  One of the directional modifiers (`.pf-m-left`, `.pf-m-top`, etc.) is required on the popover component

### Accessibility

| Attribute | Applies to | Outcome |
| -- | -- | -- |
| `role="dialog"` | `.pf-v6-c-popover` | Identifies the element that serves as the popover container. **Required** |
| `aria-labelledby="[id value of .pf-v6-c-title]"` | `.pf-v6-c-popover` | Gives the popover an accessible name by referring to the element that provides the dialog title. **Required when .pf-v6-c-title is present** |
| `aria-label="[title of popover]"` | `.pf-v6-c-popover` | Gives the popover an accessible name. **Required when .pf-v6-c-title is *not* present** |
| `aria-describedby="[id value of applicable content]"` | `.pf-v6-c-popover` | Gives the popover an accessible description by referring to the popover content that describes the primary message or purpose of the dialog. Not used if there is no static text that describes the popover. |
| `aria-modal="true"` | `.pf-v6-c-popover` | Tells assistive technologies that the windows underneath the current popover are not available for interaction. **Required**|
| `aria-label="Close"` | `.pf-v6-c-button` | Provides an accessible name for the close button as it uses an icon instead of text. **Required**|
| `aria-hidden="true"` | Parent element containing the page contents when the popover is open. | Hides main contents of the page from screen readers. The element with `.pf-v6-c-popover` must not be a descendent of the element with `aria-hidden="true"`. For more info, see [trapping focus](/accessibility/product-development-guide#trapping-focus). **Required** |
| `.pf-v6-screen-reader` | `.pf-v6-c-popover__title-text <span>` | Adds text to be read saying the alert status before the title. If `.pf-v6-c-popover__title-text` is not used to create a title, this must be added within the title. **Required for popovers that are alerts** |

### Usage

| Class | Applied to | Outcome |
| -- | -- | -- |
| `.pf-v6-c-popover` | `<div>` |  Creates a popover. Always use it with a modifier class that positions the popover relative to the element that triggered it. **Required** |
| `.pf-v6-c-popover__arrow` | `<div>` |  Creates an arrow pointing towards the element the popover describes. **Required** |
| `.pf-v6-c-popover__content` | `<div>` |  Creates the content area of the popover. **Required** |
| `.pf-v6-c-popover__close` | `<div>` |  Positions the close icon in the top-right corner of the popover. **Required if there is a close button** |
| `.pf-v6-c-popover__header` | `<header>` | Creates the popover header. **Required if there is a title**|
| `.pf-v6-c-popover__title` | `<div>` | Creates the popover title. |
| `.pf-v6-c-popover__title-icon` | `<span>` | Creates the popover title icon. |
| `.pf-v6-c-popover__title-text` | `<h1>`,`<h2>`,`<h3>`,`<h4>`,`<h5>`,`<h6>`,`<span>` | Creates the popover title text. |
| `.pf-v6-c-popover__body` | `<div>` |  The popover's body text. **Required** |
| `.pf-v6-c-popover__footer` | `<footer>` | Initiates a popover footer. |
| `.pf-m-left{-top/bottom}` | `.pf-v6-c-popover` | Positions the popover to the left (or left top/left bottom) of the element. |
| `.pf-m-right{-top/bottom}` | `.pf-v6-c-popover` | Positions the popover to the right (or right top/right bottom) of the element. |
| `.pf-m-top{-left/right}` | `.pf-v6-c-popover` | Positions the popover to the top (or top left/top right) of the element. |
| `.pf-m-bottom{-left/right}` | `.pf-v6-c-popover` | Positions the popover to the bottom (or bottom left/bottom right) of the element. |
| `.pf-m-no-padding` | `.pf-v6-c-popover` | Removes the outer padding from the popover content. |
| `.pf-m-width-auto` | `.pf-v6-c-popover` | Allows popover width to be defined by the popover content. |
| `.pf-m-custom` | `.pf-v6-c-popover` | Modifies for the custom alert state. |
| `.pf-m-info` | `.pf-v6-c-popover` | Modifies for the info alert state. |
| `.pf-m-success` | `.pf-v6-c-popover` | Modifies for the success alert state. |
| `.pf-m-warning` | `.pf-v6-c-popover` | Modifies for the warning alert state. |
| `.pf-m-danger` | `.pf-v6-c-popover` | Modifies for the danger alert state. |
