---
id: Modal
section: components
cssPrefix: pf-v6-c-modal-box
---import './ModalBox.css'

## Examples

### Basic

```html isFullscreen
<div
  class="pf-v6-c-modal-box"
  role="dialog"
  aria-modal="true"
  aria-labelledby="modal-title"
  aria-describedby="modal-description"
>
  <div class="pf-v6-c-modal-box__close">
    <button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Close">
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
  <header class="pf-v6-c-modal-box__header">
    <div class="pf-v6-c-modal-box__header-main">
      <h1 class="pf-v6-c-modal-box__title" id="modal-title">Modal title</h1>
    </div>
  </header>
  <div
    class="pf-v6-c-modal-box__body"
    id="modal-description"
  >To support screen reader user awareness of the dialog text, the dialog text is wrapped in a div that is referenced by aria-describedby.</div>
  <footer class="pf-v6-c-modal-box__footer">Modal footer</footer>
</div>

```

### With help button

```html isFullscreen
<div
  class="pf-v6-c-modal-box"
  role="dialog"
  aria-modal="true"
  aria-labelledby="modal-help-title"
  aria-describedby="modal-help-description"
>
  <div class="pf-v6-c-modal-box__close">
    <button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Close">
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
  <header class="pf-v6-c-modal-box__header pf-m-help">
    <div class="pf-v6-c-modal-box__header-main">
      <h1
        class="pf-v6-c-modal-box__title"
        id="modal-help-title"
      >Modal title Modal title Modal title Modal title Modal title Modal title Modal title Modal title</h1>
      <div
        class="pf-v6-c-modal-box__description"
        id="modal-help-description"
      >A description is used when you want to provide more info about the modal than the title is able to describe. The content in the description is static and will not scroll with the rest of the modal body.</div>
    </div>
    <div class="pf-v6-c-modal-box__header-help">
      <button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Help">
        <span class="pf-v6-c-button__icon">
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
              d="M16 1C7.729 1 1 7.729 1 16s6.729 15 15 15 15-6.729 15-15S24.271 1 16 1Zm0 28C8.832 29 3 23.168 3 16S8.832 3 16 3s13 5.832 13 13-5.832 13-13 13Zm5-17a5.008 5.008 0 0 1-4 4.899V19a1 1 0 0 1-2 0v-3a1 1 0 0 1 1-1c1.654 0 3-1.346 3-3s-1.346-3-3-3-3 1.346-3 3a1 1 0 0 1-2 0c0-2.757 2.243-5 5-5s5 2.243 5 5Zm-3.25 12a1.75 1.75 0 1 1-3.501-.001A1.75 1.75 0 0 1 17.75 24Z"
            />
          </svg>
        </span>
      </button>
    </div>
  </header>
  <div
    class="pf-v6-c-modal-box__body"
  >To support screen reader user awareness of the dialog text, the dialog text is wrapped in a div that is referenced by aria-describedby.</div>
  <footer class="pf-v6-c-modal-box__footer">Modal footer</footer>
</div>

```

### Small

```html isFullscreen
<div
  class="pf-v6-c-modal-box pf-m-sm"
  role="dialog"
  aria-modal="true"
  aria-labelledby="modal-sm-title"
  aria-describedby="modal-sm-description"
>
  <div class="pf-v6-c-modal-box__close">
    <button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Close">
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
  <header class="pf-v6-c-modal-box__header">
    <div class="pf-v6-c-modal-box__header-main">
      <h1 class="pf-v6-c-modal-box__title" id="modal-sm-title">Modal title</h1>
    </div>
  </header>
  <div class="pf-v6-c-modal-box__body" id="modal-sm-description">
    Static text describing modal purpose. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat.
  </div>
  <footer class="pf-v6-c-modal-box__footer">Modal footer</footer>
</div>

```

### Medium

```html isFullscreen
<div
  class="pf-v6-c-modal-box pf-m-md"
  role="dialog"
  aria-modal="true"
  aria-labelledby="modal-md-title"
  aria-describedby="modal-md-description"
>
  <div class="pf-v6-c-modal-box__close">
    <button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Close">
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
  <header class="pf-v6-c-modal-box__header">
    <div class="pf-v6-c-modal-box__header-main">
      <h1 class="pf-v6-c-modal-box__title" id="modal-md-title">Modal title</h1>
    </div>
  </header>
  <div class="pf-v6-c-modal-box__body" id="modal-md-description">
    Static text describing modal purpose. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat.
  </div>
  <footer class="pf-v6-c-modal-box__footer">Modal footer</footer>
</div>

```

### Large

```html isFullscreen
<div
  class="pf-v6-c-modal-box pf-m-lg"
  role="dialog"
  aria-modal="true"
  aria-labelledby="modal-lg-title"
  aria-describedby="modal-lg-description"
>
  <div class="pf-v6-c-modal-box__close">
    <button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Close">
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
  <header class="pf-v6-c-modal-box__header">
    <div class="pf-v6-c-modal-box__header-main">
      <h1 class="pf-v6-c-modal-box__title" id="modal-lg-title">Modal title</h1>
    </div>
  </header>
  <div class="pf-v6-c-modal-box__body" id="modal-lg-description">
    Static text describing modal purpose. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat.
  </div>
  <footer class="pf-v6-c-modal-box__footer">Modal footer</footer>
</div>

```

### Without title

```html isFullscreen
<div
  class="pf-v6-c-modal-box"
  role="dialog"
  aria-modal="true"
  aria-label="Example of a modal without a title"
  aria-describedby="modal-no-title-description"
>
  <div class="pf-v6-c-modal-box__close">
    <button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Close">
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
  <div class="pf-v6-c-modal-box__body">
    <span
      id="modal-no-title-description"
    >When static text describing the modal is available, it can be wrapped with an ID referring to the modal's aria-describedby value. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</span> Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
  </div>
  <footer class="pf-v6-c-modal-box__footer">Modal footer</footer>
</div>

```

### With description

```html isFullscreen
<div
  class="pf-v6-c-modal-box"
  role="dialog"
  aria-modal="true"
  aria-labelledby="modal-with-description-title"
  aria-describedby="modal-with-description-description"
>
  <div class="pf-v6-c-modal-box__close">
    <button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Close">
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
  <header class="pf-v6-c-modal-box__header">
    <div class="pf-v6-c-modal-box__header-main">
      <h1
        class="pf-v6-c-modal-box__title"
        id="modal-with-description-title"
      >Modal title</h1>
      <div
        class="pf-v6-c-modal-box__description"
        id="modal-with-description-description"
      >A description is used when you want to provide more info about the modal than the title is able to describe. The content in the description is static and will not scroll with the rest of the modal body.</div>
    </div>
  </header>
  <div
    class="pf-v6-c-modal-box__body"
  >To support screen reader user awareness of the dialog text, the dialog text is wrapped in a div that is referenced by aria-describedby.</div>
  <footer class="pf-v6-c-modal-box__footer">Modal footer</footer>
</div>

```

### Custom title

```html isFullscreen
<div
  class="pf-v6-c-modal-box"
  role="dialog"
  aria-modal="true"
  aria-labelledby="modal-custom-title"
  aria-describedby="modal-custom-description"
>
  <div class="pf-v6-c-modal-box__close">
    <button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Close">
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
  <header class="pf-v6-c-modal-box__header">
    <div class="pf-v6-c-modal-box__header-main">
      <h1 class="pf-v6-c-title pf-m-4xl" id="modal-custom-title">Custom title</h1>
    </div>
  </header>
  <div
    class="pf-v6-c-modal-box__body"
    id="modal-custom-description"
  >To support screen reader user awareness of the dialog text, the dialog text is wrapped in a div that is referenced by aria-describedby.</div>
  <footer class="pf-v6-c-modal-box__footer">Modal footer</footer>
</div>

```

### Modal box as generic container

```html isFullscreen
<div
  class="pf-v6-c-modal-box"
  role="dialog"
  aria-modal="true"
  aria-labelledby="modal-generic-container-description"
>
  <p
    id="modal-generic-container-description"
  >The modal box children elements can be removed, and the modal serves as a generic modal container. One use case of this is when creating a wizard in a modal.</p>
</div>

```

### Icon

```html isFullscreen
<div
  class="pf-v6-c-modal-box"
  role="dialog"
  aria-modal="true"
  aria-labelledby="icon-title"
  aria-describedby="icon-description"
>
  <div class="pf-v6-c-modal-box__close">
    <button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Close">
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
  <header class="pf-v6-c-modal-box__header">
    <div class="pf-v6-c-modal-box__header-main">
      <h1 class="pf-v6-c-modal-box__title pf-m-icon" id="icon-title">
        <span class="pf-v6-c-modal-box__title-icon">
          <svg
            class="pf-v6-svg"
            viewBox="0 0 36 36"
            fill="currentColor"
            aria-hidden="true"
            role="img"
            width="1em"
            height="1em"
          >
            <path
              d="M30.32 4.46a.63.63 0 0 0-.61 0l-14.87 7.92H11a5.62 5.62 0 0 0-1.24 11.1l1.63 7.65a.64.64 0 0 0 .61.49h3a.62.62 0 0 0 .62-.62v-7l14.09 7.51a.62.62 0 0 0 .91-.55V5a.63.63 0 0 0-.3-.54ZM14.38 30.38h-1.87l-1.44-6.76h3.31Zm0-8H11a4.38 4.38 0 0 1 0-8.76h3.38Zm15 7.58-13.76-7.34v-9.24L29.38 6Z"
            />
          </svg>
        </span>
        <span class="pf-v6-c-modal-box__title-text">Modal with icon title</span>
      </h1>
    </div>
  </header>
  <div class="pf-v6-c-modal-box__body" id="icon-description">Modal description</div>
  <footer class="pf-v6-c-modal-box__footer">Modal footer</footer>
</div>

```

### Custom alert

```html isFullscreen
<div
  class="pf-v6-c-modal-box pf-m-custom"
  role="dialog"
  aria-modal="true"
  aria-labelledby="custom-alert-title"
  aria-describedby="custom-alert-description"
>
  <div class="pf-v6-c-modal-box__close">
    <button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Close">
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
  <header class="pf-v6-c-modal-box__header">
    <div class="pf-v6-c-modal-box__header-main">
      <h1 class="pf-v6-c-modal-box__title pf-m-icon" id="custom-alert-title">
        <span class="pf-v6-c-modal-box__title-icon">
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
        <span class="pf-v6-u-screen-reader">
          Default
          alert:
        </span>
        <span class="pf-v6-c-modal-box__title-text">Custom alert modal title</span>
      </h1>
    </div>
  </header>
  <div
    class="pf-v6-c-modal-box__body"
    id="custom-alert-description"
  >Modal description</div>
  <footer class="pf-v6-c-modal-box__footer">Modal footer</footer>
</div>

```

### Info alert

```html isFullscreen
<div
  class="pf-v6-c-modal-box pf-m-info"
  role="dialog"
  aria-modal="true"
  aria-labelledby="info-alert-title"
  aria-describedby="info-alert-description"
>
  <div class="pf-v6-c-modal-box__close">
    <button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Close">
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
  <header class="pf-v6-c-modal-box__header">
    <div class="pf-v6-c-modal-box__header-main">
      <h1 class="pf-v6-c-modal-box__title pf-m-icon" id="info-alert-title">
        <span class="pf-v6-c-modal-box__title-icon">
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
        <span class="pf-v6-u-screen-reader">
          Info
          alert:
        </span>
        <span class="pf-v6-c-modal-box__title-text">Info alert modal title</span>
      </h1>
    </div>
  </header>
  <div
    class="pf-v6-c-modal-box__body"
    id="info-alert-description"
  >Modal description</div>
  <footer class="pf-v6-c-modal-box__footer">Modal footer</footer>
</div>

```

### Success alert

```html isFullscreen
<div
  class="pf-v6-c-modal-box pf-m-success"
  role="dialog"
  aria-modal="true"
  aria-labelledby="success-alert-title"
  aria-describedby="success-alert-description"
>
  <div class="pf-v6-c-modal-box__close">
    <button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Close">
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
  <header class="pf-v6-c-modal-box__header">
    <div class="pf-v6-c-modal-box__header-main">
      <h1 class="pf-v6-c-modal-box__title pf-m-icon" id="success-alert-title">
        <span class="pf-v6-c-modal-box__title-icon">
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
        <span class="pf-v6-u-screen-reader">
          Success
          alert:
        </span>
        <span class="pf-v6-c-modal-box__title-text">Success alert modal title</span>
      </h1>
    </div>
  </header>
  <div
    class="pf-v6-c-modal-box__body"
    id="success-alert-description"
  >Modal description</div>
  <footer class="pf-v6-c-modal-box__footer">Modal footer</footer>
</div>

```

### Warning alert

```html isFullscreen
<div
  class="pf-v6-c-modal-box pf-m-warning"
  role="dialog"
  aria-modal="true"
  aria-labelledby="warning-alert-title"
  aria-describedby="warning-alert-description"
>
  <div class="pf-v6-c-modal-box__close">
    <button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Close">
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
  <header class="pf-v6-c-modal-box__header">
    <div class="pf-v6-c-modal-box__header-main">
      <h1 class="pf-v6-c-modal-box__title pf-m-icon" id="warning-alert-title">
        <span class="pf-v6-c-modal-box__title-icon">
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
        <span class="pf-v6-u-screen-reader">
          Warning
          alert:
        </span>
        <span class="pf-v6-c-modal-box__title-text">Warning alert modal title</span>
      </h1>
    </div>
  </header>
  <div
    class="pf-v6-c-modal-box__body"
    id="warning-alert-description"
  >Modal description</div>
  <footer class="pf-v6-c-modal-box__footer">Modal footer</footer>
</div>

```

### Danger alert

```html isFullscreen
<div
  class="pf-v6-c-modal-box pf-m-danger"
  role="dialog"
  aria-modal="true"
  aria-labelledby="danger-alert-title"
  aria-describedby="danger-alert-description"
>
  <div class="pf-v6-c-modal-box__close">
    <button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Close">
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
  <header class="pf-v6-c-modal-box__header">
    <div class="pf-v6-c-modal-box__header-main">
      <h1 class="pf-v6-c-modal-box__title pf-m-icon" id="danger-alert-title">
        <span class="pf-v6-c-modal-box__title-icon">
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
        <span class="pf-v6-u-screen-reader">
          Danger
          alert:
        </span>
        <span class="pf-v6-c-modal-box__title-text">Danger alert modal title</span>
      </h1>
    </div>
  </header>
  <div
    class="pf-v6-c-modal-box__body"
    id="danger-alert-description"
  >To support screen reader user awareness of the dialog text, the dialog text is wrapped in a div that is referenced by aria-describedby.</div>
  <footer class="pf-v6-c-modal-box__footer">Modal footer</footer>
</div>

```

### Danger alert with modifier on modal title

The status modifier classes can be applied directly to the modal title element, instead of the parent modal.

```html isFullscreen
<div
  class="pf-v6-c-modal-box"
  role="dialog"
  aria-modal="true"
  aria-labelledby="danger-alert-title-title"
  aria-describedby="danger-alert-title-description"
>
  <div class="pf-v6-c-modal-box__close">
    <button class="pf-v6-c-button pf-m-plain" type="button" aria-label="Close">
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
  <header class="pf-v6-c-modal-box__header">
    <div class="pf-v6-c-modal-box__header-main">
      <h1
        class="pf-v6-c-modal-box__title pf-m-icon pf-m-danger"
        id="danger-alert-title-title"
      >
        <span class="pf-v6-c-modal-box__title-icon">
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
        <span class="pf-v6-u-screen-reader">
          Danger
          alert:
        </span>
        <span class="pf-v6-c-modal-box__title-text">Danger alert modal title</span>
      </h1>
    </div>
  </header>
  <div
    class="pf-v6-c-modal-box__body"
    id="danger-alert-title-description"
  >To support screen reader user awareness of the dialog text, the dialog text is wrapped in a div that is referenced by aria-describedby.</div>
  <footer class="pf-v6-c-modal-box__footer">Modal footer</footer>
</div>

```

## Documentation

### Overview

A modal box is a generic rectangular container that can be used to build modals. A modal box can have the following sections: header, title, description, body, and footer. With normal use of the modal, a title or body is required. Alternatively, no child elements can be used, and the `.pf-v6-c-modal-box` container will  serve as a generic container with no padding for custom modal content. If no `.pf-v6-c-modal-box__title` is used, `aria-label="[title of modal]"` must be provided for `.pf-v6-c-modal-box`.

### Accessibility

| Attribute | Applies to | Outcome |
| -- | -- | -- |
| `role="dialog"` | `.pf-v6-c-modal-box` | Identifies the element that serves as the modal container. **Required** |
| `aria-labelledby="[id value of .pf-v6-c-modal-box__title or custom modal title]"` | `.pf-v6-c-modal-box` | Gives the modal an accessible name by referring to the element that provides the dialog title. **Required when .pf-v6-c-title is present** |
| `aria-label="[title of modal]"` | `.pf-v6-c-modal-box` | Gives the modal an accessible name. **Required when `.pf-v6-c-modal-box__title` is *not* present** |
| `aria-describedby="[id value of applicable content]"` | `.pf-v6-c-modal-box` | Gives the modal an accessible description by referring to the modal content that describes the primary message or purpose of the dialog. Not used if there is no static text that describes the modal. |
| `aria-modal="true"` | `.pf-v6-c-modal-box` | Tells assistive technologies that the windows underneath the current modal are not available for interaction. **Required**|
| `aria-label="Close"` | `.pf-v6-c-modal-box__close .pf-v6-c-button` | Provides an accessible name for the close button as it uses an icon instead of text. **Required**|
| `aria-hidden="true"` | Parent element containing the page contents when modal is open | Hides main contents of the page from screen readers. The element with `.pf-v6-c-modal-box` must not be a descendent of the element with `aria-hidden="true"`. For more info see [trapping focus](/accessibility/develop#trapping-focus). **Required** |
| `form="[id of form in modal body]"` | `.pf-v6-c-modal-box__footer .pf-v6-c-button` | Associates a submit button in the modal footer with a form in the modal body. For use when the submit button is outside of the `<form>` that the button submits. |
| `tabindex="0"` | `.pf-v6-c-modal-box__body` | If a modal box body has overflow content that triggers a scrollbar, to ensure that the content is keyboard accessible, the body must include either a focusable element within the scrollable region or the body itself must be focusable by adding `tabindex="0"`. |

### Usage

| Class | Applied | Outcome |
| -- | -- | -- |
| `.pf-v6-c-modal-box` | `<div>` | Initiates a modal box. **Required** |
| `.pf-v6-c-modal-box__close` | `<div>` | Creates a container for the modal box close button. **Required** if there is a close button. |
| `.pf-v6-c-button.pf-m-plain` | `<button>` | Initiates a modal box close button. |
| `.pf-v6-c-modal-box__header` | `<header>` | Initiates a modal box header. **Required** if using a `.pf-v6-c-modal-box__title`. |
| `.pf-v6-c-modal-box__header-main` | `<div>` | Initiates a modal box header main container. **Required** when using a modal header. |
| `.pf-v6-c-modal-box__header-help` | `<div>` | Initiates the help button container in the modal box header actions. |
| `.pf-v6-c-modal-box__title` | `<h1>`,`<h2>`,`<h3>`,`<h4>`,`<h5>`,`<h6>`, `<div>` | Initiates a modal box title. **Required** if using a modal description. |
| `.pf-v6-c-modal-box__title-icon` | `<span>` | Initiates a container for the modal box title icon. |
| `.pf-v6-c-modal-box__title-text` | `<span>` | Initiates a container for the modal box title text. |
| `.pf-v6-c-modal-box__description` | `<div>` | Initiates a modal box description. |
| `.pf-v6-c-modal-box__body` | `<div>` | Initiates a modal box body. |
| `.pf-v6-c-modal-box__footer` | `<footer>` | Initiates a modal box footer. |
| `.pf-m-sm` | `.pf-v6-c-modal-box` | Modifies for a small modal box width. |
| `.pf-m-md` | `.pf-v6-c-modal-box` | Modifies for a medium modal box width. |
| `.pf-m-lg` | `.pf-v6-c-modal-box` | Modifies for a large modal box width. |
| `.pf-m-align-top` | `.pf-v6-c-modal-box` | Modifies for top alignment.  |
| `.pf-m-icon` | `.pf-v6-c-modal-box__title` | Modifies the title layout to accommodate an icon. |
| `.pf-m-custom` | `.pf-v6-c-modal-box`, `.pf-v6-c-modal-box__title` | Modifies for the custom alert state. |
| `.pf-m-info` | `.pf-v6-c-modal-box`, `.pf-v6-c-modal-box__title` | Modifies for the info alert state. |
| `.pf-m-success` | `.pf-v6-c-modal-box`, `.pf-v6-c-modal-box__title` | Modifies for the success alert state. |
| `.pf-m-warning` | `.pf-v6-c-modal-box`, `.pf-v6-c-modal-box__title` | Modifies for the warning alert state. |
| `.pf-m-danger` | `.pf-v6-c-modal-box`, `.pf-v6-c-modal-box__title` | Modifies for the danger alert state. |
| `.pf-m-help` | `.pf-v6-c-modal-box__header` | Modifies the modal box header to support the help action |
