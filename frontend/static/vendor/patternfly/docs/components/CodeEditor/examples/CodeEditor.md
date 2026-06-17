---
id: Code editor
section: components
cssPrefix: pf-v6-c-code-editor
---import './CodeEditor.css';

## Examples

### Default

```html
<div class="pf-v6-c-code-editor">
  <div class="pf-v6-c-code-editor__header">
    <div class="pf-v6-c-code-editor__header-content">
      <div class="pf-v6-c-code-editor__controls">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Copy to clipboard"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 448 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M320 448v40c0 13.255-10.745 24-24 24H24c-13.255 0-24-10.745-24-24V120c0-13.255 10.745-24 24-24h72v296c0 30.879 25.121 56 56 56h168zm0-344V0H152c-13.255 0-24 10.745-24 24v368c0 13.255 10.745 24 24 24h272c13.255 0 24-10.745 24-24V128H344c-13.2 0-24-10.8-24-24zm120.971-31.029L375.029 7.029A24 24 0 0 0 358.059 0H352v96h96v-6.059a24 24 0 0 0-7.029-16.97z"
              />
            </svg>
          </span>
        </button>
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Download code"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 512 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M216 0h80c13.3 0 24 10.7 24 24v168h87.7c17.8 0 26.7 21.5 14.1 34.1L269.7 378.3c-7.5 7.5-19.8 7.5-27.3 0L90.1 226.1c-12.6-12.6-3.7-34.1 14.1-34.1H192V24c0-13.3 10.7-24 24-24zm296 376v112c0 13.3-10.7 24-24 24H24c-13.3 0-24-10.7-24-24V376c0-13.3 10.7-24 24-24h146.7l49 49c20.1 20.1 52.5 20.1 72.6 0l49-49H488c13.3 0 24 10.7 24 24zm-124 88c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20zm64 0c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20z"
              />
            </svg>
          </span>
        </button>
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Upload code"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 512 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M296 384h-80c-13.3 0-24-10.7-24-24V192h-87.7c-17.8 0-26.7-21.5-14.1-34.1L242.3 5.7c7.5-7.5 19.8-7.5 27.3 0l152.2 152.2c12.6 12.6 3.7 34.1-14.1 34.1H320v168c0 13.3-10.7 24-24 24zm216-8v112c0 13.3-10.7 24-24 24H24c-13.3 0-24-10.7-24-24V376c0-13.3 10.7-24 24-24h136v8c0 30.9 25.1 56 56 56h80c30.9 0 56-25.1 56-56v-8h136c13.3 0 24 10.7 24 24zm-124 88c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20zm64 0c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20z"
              />
            </svg>
          </span>
        </button>
      </div>
      <div class="pf-v6-c-code-editor__header-main"></div>
    </div>
    <div class="pf-v6-c-code-editor__tab">
      <span class="pf-v6-c-code-editor__tab-icon">
        <i class="fas fa-code"></i>
      </span>
      <span class="pf-v6-c-code-editor__tab-text">HTML</span>
    </div>
  </div>
  <div class="pf-v6-c-code-editor__main">
    <div dir="ltr" class="pf-v6-c-code-editor__code">
      <pre class="pf-v6-c-code-editor__code-pre">
                code goes here
      </pre>
    </div>
  </div>
</div>

```

### Read-only

```html
<div class="pf-v6-c-code-editor pf-m-read-only">
  <div class="pf-v6-c-code-editor__header">
    <div class="pf-v6-c-code-editor__header-content">
      <div class="pf-v6-c-code-editor__controls">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Copy to clipboard"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 448 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M320 448v40c0 13.255-10.745 24-24 24H24c-13.255 0-24-10.745-24-24V120c0-13.255 10.745-24 24-24h72v296c0 30.879 25.121 56 56 56h168zm0-344V0H152c-13.255 0-24 10.745-24 24v368c0 13.255 10.745 24 24 24h272c13.255 0 24-10.745 24-24V128H344c-13.2 0-24-10.8-24-24zm120.971-31.029L375.029 7.029A24 24 0 0 0 358.059 0H352v96h96v-6.059a24 24 0 0 0-7.029-16.97z"
              />
            </svg>
          </span>
        </button>
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Download code"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 512 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M216 0h80c13.3 0 24 10.7 24 24v168h87.7c17.8 0 26.7 21.5 14.1 34.1L269.7 378.3c-7.5 7.5-19.8 7.5-27.3 0L90.1 226.1c-12.6-12.6-3.7-34.1 14.1-34.1H192V24c0-13.3 10.7-24 24-24zm296 376v112c0 13.3-10.7 24-24 24H24c-13.3 0-24-10.7-24-24V376c0-13.3 10.7-24 24-24h146.7l49 49c20.1 20.1 52.5 20.1 72.6 0l49-49H488c13.3 0 24 10.7 24 24zm-124 88c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20zm64 0c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20z"
              />
            </svg>
          </span>
        </button>
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Upload code"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 512 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M296 384h-80c-13.3 0-24-10.7-24-24V192h-87.7c-17.8 0-26.7-21.5-14.1-34.1L242.3 5.7c7.5-7.5 19.8-7.5 27.3 0l152.2 152.2c12.6 12.6 3.7 34.1-14.1 34.1H320v168c0 13.3-10.7 24-24 24zm216-8v112c0 13.3-10.7 24-24 24H24c-13.3 0-24-10.7-24-24V376c0-13.3 10.7-24 24-24h136v8c0 30.9 25.1 56 56 56h80c30.9 0 56-25.1 56-56v-8h136c13.3 0 24 10.7 24 24zm-124 88c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20zm64 0c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20z"
              />
            </svg>
          </span>
        </button>
      </div>
      <div class="pf-v6-c-code-editor__header-main"></div>
    </div>
    <div class="pf-v6-c-code-editor__tab">
      <span class="pf-v6-c-code-editor__tab-icon">
        <i class="fas fa-code"></i>
      </span>
      <span class="pf-v6-c-code-editor__tab-text">HTML</span>
    </div>
  </div>
  <div class="pf-v6-c-code-editor__main">
    <div dir="ltr" class="pf-v6-c-code-editor__code">
      <pre class="pf-v6-c-code-editor__code-pre">
                code goes here
      </pre>
    </div>
  </div>
</div>

```

### Without actions

```html
<div class="pf-v6-c-code-editor">
  <div class="pf-v6-c-code-editor__header">
    <div class="pf-v6-c-code-editor__tab">
      <span class="pf-v6-c-code-editor__tab-icon">
        <i class="fas fa-code" aria-hidden="true"></i>
      </span>
      <span class="pf-v6-c-code-editor__tab-text">YAML</span>
    </div>
  </div>
  <div class="pf-v6-c-code-editor__main">
    <div class="pf-v6-c-code-editor__upload">
      <div class="pf-v6-c-empty-state">
        <div class="pf-v6-c-empty-state__content">
          <div class="pf-v6-c-empty-state__header">
            <div class="pf-v6-c-empty-state__icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 640 512"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M278.9 511.5l-61-17.7c-6.4-1.8-10-8.5-8.2-14.9L346.2 8.7c1.8-6.4 8.5-10 14.9-8.2l61 17.7c6.4 1.8 10 8.5 8.2 14.9L293.8 503.3c-1.9 6.4-8.5 10.1-14.9 8.2zm-114-112.2l43.5-46.4c4.6-4.9 4.3-12.7-.8-17.2L117 256l90.6-79.7c5.1-4.5 5.5-12.3.8-17.2l-43.5-46.4c-4.5-4.8-12.1-5.1-17-.5L3.8 247.2c-5.1 4.7-5.1 12.8 0 17.5l144.1 135.1c4.9 4.6 12.5 4.4 17-.5zm327.2.6l144.1-135.1c5.1-4.7 5.1-12.8 0-17.5L492.1 112.1c-4.8-4.5-12.4-4.3-17 .5L431.6 159c-4.6 4.9-4.3 12.7.8 17.2L523 256l-90.6 79.7c-5.1 4.5-5.5 12.3-.8 17.2l43.5 46.4c4.5 4.9 12.1 5.1 17 .6z"
                />
              </svg>
            </div>
            <div class="pf-v6-c-empty-state__title">
              <h4 class="pf-v6-c-empty-state__title-text">Start editing</h4>
            </div>
          </div>

          <div
            class="pf-v6-c-empty-state__body"
          >Drag a file here or browse to upload.</div>

          <div class="pf-v6-c-empty-state__footer">
            <div class="pf-v6-c-empty-state__actions">
              <button class="pf-v6-c-button pf-m-primary" type="button">
                <span class="pf-v6-c-button__text">Browse</span>
              </button>
            </div>
            <div class="pf-v6-c-empty-state__actions">
              <button class="pf-v6-c-button pf-m-link" type="button">
                <span class="pf-v6-c-button__text">Start from scratch</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

```

### Without language tab

```html
<div class="pf-v6-c-code-editor">
  <div class="pf-v6-c-code-editor__header"></div>
  <div class="pf-v6-c-code-editor__main">
    <div dir="ltr" class="pf-v6-c-code-editor__code">
      <pre class="pf-v6-c-code-editor__code-pre">
                code goes here
      </pre>
    </div>
  </div>
</div>

```

### Drag file and hover over component

```html
<div class="pf-v6-c-code-editor">
  <div class="pf-v6-c-code-editor__header">
    <div class="pf-v6-c-code-editor__tab">
      <span class="pf-v6-c-code-editor__tab-icon">
        <i class="fas fa-code" aria-hidden="true"></i>
      </span>
      <span class="pf-v6-c-code-editor__tab-text">YAML</span>
    </div>
  </div>
  <div class="pf-v6-c-code-editor__main pf-m-drag-hover">
    <div class="pf-v6-c-code-editor__upload">
      <div class="pf-v6-c-empty-state">
        <div class="pf-v6-c-empty-state__content">
          <div class="pf-v6-c-empty-state__header">
            <div class="pf-v6-c-empty-state__icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 640 512"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M278.9 511.5l-61-17.7c-6.4-1.8-10-8.5-8.2-14.9L346.2 8.7c1.8-6.4 8.5-10 14.9-8.2l61 17.7c6.4 1.8 10 8.5 8.2 14.9L293.8 503.3c-1.9 6.4-8.5 10.1-14.9 8.2zm-114-112.2l43.5-46.4c4.6-4.9 4.3-12.7-.8-17.2L117 256l90.6-79.7c5.1-4.5 5.5-12.3.8-17.2l-43.5-46.4c-4.5-4.8-12.1-5.1-17-.5L3.8 247.2c-5.1 4.7-5.1 12.8 0 17.5l144.1 135.1c4.9 4.6 12.5 4.4 17-.5zm327.2.6l144.1-135.1c5.1-4.7 5.1-12.8 0-17.5L492.1 112.1c-4.8-4.5-12.4-4.3-17 .5L431.6 159c-4.6 4.9-4.3 12.7.8 17.2L523 256l-90.6 79.7c-5.1 4.5-5.5 12.3-.8 17.2l43.5 46.4c4.5 4.9 12.1 5.1 17 .6z"
                />
              </svg>
            </div>
            <div class="pf-v6-c-empty-state__title">
              <h4 class="pf-v6-c-empty-state__title-text">Start editing</h4>
            </div>
          </div>

          <div
            class="pf-v6-c-empty-state__body"
          >Drag a file here or browse to upload.</div>

          <div class="pf-v6-c-empty-state__footer">
            <div class="pf-v6-c-empty-state__actions">
              <button class="pf-v6-c-button pf-m-primary" type="button">
                <span class="pf-v6-c-button__text">Browse</span>
              </button>
            </div>
            <div class="pf-v6-c-empty-state__actions">
              <button class="pf-v6-c-button pf-m-link" type="button">
                <span class="pf-v6-c-button__text">Start from scratch</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

```

### With optional header content and keyboard shortcuts

```html
<div class="pf-v6-c-code-editor">
  <div class="pf-v6-c-code-editor__header">
    <div class="pf-v6-c-code-editor__header-content">
      <div class="pf-v6-c-code-editor__controls">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Copy to clipboard"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 448 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M320 448v40c0 13.255-10.745 24-24 24H24c-13.255 0-24-10.745-24-24V120c0-13.255 10.745-24 24-24h72v296c0 30.879 25.121 56 56 56h168zm0-344V0H152c-13.255 0-24 10.745-24 24v368c0 13.255 10.745 24 24 24h272c13.255 0 24-10.745 24-24V128H344c-13.2 0-24-10.8-24-24zm120.971-31.029L375.029 7.029A24 24 0 0 0 358.059 0H352v96h96v-6.059a24 24 0 0 0-7.029-16.97z"
              />
            </svg>
          </span>
        </button>
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Download code"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 512 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M216 0h80c13.3 0 24 10.7 24 24v168h87.7c17.8 0 26.7 21.5 14.1 34.1L269.7 378.3c-7.5 7.5-19.8 7.5-27.3 0L90.1 226.1c-12.6-12.6-3.7-34.1 14.1-34.1H192V24c0-13.3 10.7-24 24-24zm296 376v112c0 13.3-10.7 24-24 24H24c-13.3 0-24-10.7-24-24V376c0-13.3 10.7-24 24-24h146.7l49 49c20.1 20.1 52.5 20.1 72.6 0l49-49H488c13.3 0 24 10.7 24 24zm-124 88c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20zm64 0c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20z"
              />
            </svg>
          </span>
        </button>
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Upload code"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 512 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M296 384h-80c-13.3 0-24-10.7-24-24V192h-87.7c-17.8 0-26.7-21.5-14.1-34.1L242.3 5.7c7.5-7.5 19.8-7.5 27.3 0l152.2 152.2c12.6 12.6 3.7 34.1-14.1 34.1H320v168c0 13.3-10.7 24-24 24zm216-8v112c0 13.3-10.7 24-24 24H24c-13.3 0-24-10.7-24-24V376c0-13.3 10.7-24 24-24h136v8c0 30.9 25.1 56 56 56h80c30.9 0 56-25.1 56-56v-8h136c13.3 0 24 10.7 24 24zm-124 88c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20zm64 0c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20z"
              />
            </svg>
          </span>
        </button>
      </div>
      <div class="pf-v6-c-code-editor__header-main">Header main content</div>
      <div class="pf-v6-c-code-editor__keyboard-shortcuts">
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__icon pf-m-start">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 1024 1024"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M521.3,576 C627.5,576 713.7,502 713.7,413.7 C713.7,325.4 627.6,253.6 521.3,253.6 C366,253.6 334.5,337.7 329.2,407.2 C329.2,414.3 335.2,416 343.5,416 L445,416 C450.5,416 458,415.5 460.8,406.5 C460.8,362.6 582.9,357.1 582.9,413.6 C582.9,441.9 556.2,470.9 521.3,473 C486.4,475.1 447.3,479.8 447.3,521.7 L447.3,553.8 C447.3,570.8 456.1,576 472,576 C487.9,576 521.3,576 521.3,576 M575.3,751.3 L575.3,655.3 C575.313862,651.055109 573.620137,646.982962 570.6,644 C567.638831,640.947672 563.552355,639.247987 559.3,639.29884 L463.3,639.29884 C459.055109,639.286138 454.982962,640.979863 452,644 C448.947672,646.961169 447.247987,651.047645 447.29884,655.3 L447.29884,751.3 C447.286138,755.544891 448.979863,759.617038 452,762.6 C454.961169,765.652328 459.047645,767.352013 463.3,767.30116 L559.3,767.30116 C563.544891,767.313862 567.617038,765.620137 570.6,762.6 C573.659349,759.643612 575.360354,755.553963 575.3,751.3 M512,896 C300.2,896 128,723.9 128,512 C128,300.3 300.2,128 512,128 C723.8,128 896,300.2 896,512 C896,723.8 723.7,896 512,896 M512.1,0 C229.7,0 0,229.8 0,512 C0,794.2 229.8,1024 512.1,1024 C794.4,1024 1024,794.3 1024,512 C1024,229.7 794.4,0 512.1,0"
              />
            </svg>
          </span>
          <span class="pf-v6-c-button__text">View shortcuts</span>
        </button>
      </div>
    </div>
    <div class="pf-v6-c-code-editor__tab">
      <span class="pf-v6-c-code-editor__tab-icon">
        <i class="fas fa-code"></i>
      </span>
      <span class="pf-v6-c-code-editor__tab-text">HTML</span>
    </div>
  </div>
  <div class="pf-v6-c-code-editor__main">
    <div dir="ltr" class="pf-v6-c-code-editor__code">
      <pre class="pf-v6-c-code-editor__code-pre">
                code goes here
      </pre>
    </div>
  </div>
</div>

```

### With optional code editor container

This is an extra container used in React to prevent event propagation if upload is enabled or there is a provided empty state.

```html
<div class="pf-v6-c-code-editor">
  <div role="presentation" tabindex="0" class="pf-v6-c-code-editor__container">
    <div class="pf-v6-c-code-editor__header">
      <div class="pf-v6-c-code-editor__header-content">
        <div class="pf-v6-c-code-editor__controls">
          <button
            class="pf-v6-c-button pf-m-plain"
            type="button"
            aria-label="Copy to clipboard"
          >
            <span class="pf-v6-c-button__icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 448 512"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M320 448v40c0 13.255-10.745 24-24 24H24c-13.255 0-24-10.745-24-24V120c0-13.255 10.745-24 24-24h72v296c0 30.879 25.121 56 56 56h168zm0-344V0H152c-13.255 0-24 10.745-24 24v368c0 13.255 10.745 24 24 24h272c13.255 0 24-10.745 24-24V128H344c-13.2 0-24-10.8-24-24zm120.971-31.029L375.029 7.029A24 24 0 0 0 358.059 0H352v96h96v-6.059a24 24 0 0 0-7.029-16.97z"
                />
              </svg>
            </span>
          </button>
          <button
            class="pf-v6-c-button pf-m-plain"
            type="button"
            aria-label="Download code"
          >
            <span class="pf-v6-c-button__icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 512 512"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M216 0h80c13.3 0 24 10.7 24 24v168h87.7c17.8 0 26.7 21.5 14.1 34.1L269.7 378.3c-7.5 7.5-19.8 7.5-27.3 0L90.1 226.1c-12.6-12.6-3.7-34.1 14.1-34.1H192V24c0-13.3 10.7-24 24-24zm296 376v112c0 13.3-10.7 24-24 24H24c-13.3 0-24-10.7-24-24V376c0-13.3 10.7-24 24-24h146.7l49 49c20.1 20.1 52.5 20.1 72.6 0l49-49H488c13.3 0 24 10.7 24 24zm-124 88c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20zm64 0c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20z"
                />
              </svg>
            </span>
          </button>
          <button
            class="pf-v6-c-button pf-m-plain"
            type="button"
            aria-label="Upload code"
          >
            <span class="pf-v6-c-button__icon">
              <svg
                class="pf-v6-svg"
                viewBox="0 0 512 512"
                fill="currentColor"
                aria-hidden="true"
                role="img"
                width="1em"
                height="1em"
              >
                <path
                  d="M296 384h-80c-13.3 0-24-10.7-24-24V192h-87.7c-17.8 0-26.7-21.5-14.1-34.1L242.3 5.7c7.5-7.5 19.8-7.5 27.3 0l152.2 152.2c12.6 12.6 3.7 34.1-14.1 34.1H320v168c0 13.3-10.7 24-24 24zm216-8v112c0 13.3-10.7 24-24 24H24c-13.3 0-24-10.7-24-24V376c0-13.3 10.7-24 24-24h136v8c0 30.9 25.1 56 56 56h80c30.9 0 56-25.1 56-56v-8h136c13.3 0 24 10.7 24 24zm-124 88c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20zm64 0c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20z"
                />
              </svg>
            </span>
          </button>
        </div>
      </div>
      <div class="pf-v6-c-code-editor__tab">
        <span class="pf-v6-c-code-editor__tab-icon">
          <i class="fas fa-code"></i>
        </span>
        <span class="pf-v6-c-code-editor__tab-text">HTML</span>
      </div>
    </div>
    <div class="pf-v6-c-code-editor__main">
      <div class="pf-v6-c-code-editor__upload">
        <div class="pf-v6-c-empty-state">
          <div class="pf-v6-c-empty-state__content">
            <div class="pf-v6-c-empty-state__header">
              <div class="pf-v6-c-empty-state__icon">
                <svg
                  class="pf-v6-svg"
                  viewBox="0 0 640 512"
                  fill="currentColor"
                  aria-hidden="true"
                  role="img"
                  width="1em"
                  height="1em"
                >
                  <path
                    d="M278.9 511.5l-61-17.7c-6.4-1.8-10-8.5-8.2-14.9L346.2 8.7c1.8-6.4 8.5-10 14.9-8.2l61 17.7c6.4 1.8 10 8.5 8.2 14.9L293.8 503.3c-1.9 6.4-8.5 10.1-14.9 8.2zm-114-112.2l43.5-46.4c4.6-4.9 4.3-12.7-.8-17.2L117 256l90.6-79.7c5.1-4.5 5.5-12.3.8-17.2l-43.5-46.4c-4.5-4.8-12.1-5.1-17-.5L3.8 247.2c-5.1 4.7-5.1 12.8 0 17.5l144.1 135.1c4.9 4.6 12.5 4.4 17-.5zm327.2.6l144.1-135.1c5.1-4.7 5.1-12.8 0-17.5L492.1 112.1c-4.8-4.5-12.4-4.3-17 .5L431.6 159c-4.6 4.9-4.3 12.7.8 17.2L523 256l-90.6 79.7c-5.1 4.5-5.5 12.3-.8 17.2l43.5 46.4c4.5 4.9 12.1 5.1 17 .6z"
                  />
                </svg>
              </div>
              <div class="pf-v6-c-empty-state__title">
                <h4 class="pf-v6-c-empty-state__title-text">Start editing</h4>
              </div>
            </div>

            <div
              class="pf-v6-c-empty-state__body"
            >Drag a file here or browse to upload.</div>

            <div class="pf-v6-c-empty-state__footer">
              <div class="pf-v6-c-empty-state__actions">
                <button class="pf-v6-c-button pf-m-primary" type="button">
                  <span class="pf-v6-c-button__text">Browse</span>
                </button>
              </div>
              <div class="pf-v6-c-empty-state__actions">
                <button class="pf-v6-c-button pf-m-link" type="button">
                  <span class="pf-v6-c-button__text">Start from scratch</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

```

### With full height modifier

```html
<div class="pf-v6-c-code-editor pf-m-full-height">
  <div class="pf-v6-c-code-editor__header">
    <div class="pf-v6-c-code-editor__header-content">
      <div class="pf-v6-c-code-editor__controls">
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Copy to clipboard"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 448 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M320 448v40c0 13.255-10.745 24-24 24H24c-13.255 0-24-10.745-24-24V120c0-13.255 10.745-24 24-24h72v296c0 30.879 25.121 56 56 56h168zm0-344V0H152c-13.255 0-24 10.745-24 24v368c0 13.255 10.745 24 24 24h272c13.255 0 24-10.745 24-24V128H344c-13.2 0-24-10.8-24-24zm120.971-31.029L375.029 7.029A24 24 0 0 0 358.059 0H352v96h96v-6.059a24 24 0 0 0-7.029-16.97z"
              />
            </svg>
          </span>
        </button>
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Download code"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 512 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M216 0h80c13.3 0 24 10.7 24 24v168h87.7c17.8 0 26.7 21.5 14.1 34.1L269.7 378.3c-7.5 7.5-19.8 7.5-27.3 0L90.1 226.1c-12.6-12.6-3.7-34.1 14.1-34.1H192V24c0-13.3 10.7-24 24-24zm296 376v112c0 13.3-10.7 24-24 24H24c-13.3 0-24-10.7-24-24V376c0-13.3 10.7-24 24-24h146.7l49 49c20.1 20.1 52.5 20.1 72.6 0l49-49H488c13.3 0 24 10.7 24 24zm-124 88c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20zm64 0c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20z"
              />
            </svg>
          </span>
        </button>
        <button
          class="pf-v6-c-button pf-m-plain"
          type="button"
          aria-label="Upload code"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 512 512"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M296 384h-80c-13.3 0-24-10.7-24-24V192h-87.7c-17.8 0-26.7-21.5-14.1-34.1L242.3 5.7c7.5-7.5 19.8-7.5 27.3 0l152.2 152.2c12.6 12.6 3.7 34.1-14.1 34.1H320v168c0 13.3-10.7 24-24 24zm216-8v112c0 13.3-10.7 24-24 24H24c-13.3 0-24-10.7-24-24V376c0-13.3 10.7-24 24-24h136v8c0 30.9 25.1 56 56 56h80c30.9 0 56-25.1 56-56v-8h136c13.3 0 24 10.7 24 24zm-124 88c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20zm64 0c0-11-9-20-20-20s-20 9-20 20 9 20 20 20 20-9 20-20z"
              />
            </svg>
          </span>
        </button>
      </div>
      <div class="pf-v6-c-code-editor__header-main">Header main content</div>
      <div class="pf-v6-c-code-editor__keyboard-shortcuts">
        <button class="pf-v6-c-button pf-m-link" type="button">
          <span class="pf-v6-c-button__icon pf-m-start">
            <svg
              class="pf-v6-svg"
              viewBox="0 0 1024 1024"
              fill="currentColor"
              aria-hidden="true"
              role="img"
              width="1em"
              height="1em"
            >
              <path
                d="M521.3,576 C627.5,576 713.7,502 713.7,413.7 C713.7,325.4 627.6,253.6 521.3,253.6 C366,253.6 334.5,337.7 329.2,407.2 C329.2,414.3 335.2,416 343.5,416 L445,416 C450.5,416 458,415.5 460.8,406.5 C460.8,362.6 582.9,357.1 582.9,413.6 C582.9,441.9 556.2,470.9 521.3,473 C486.4,475.1 447.3,479.8 447.3,521.7 L447.3,553.8 C447.3,570.8 456.1,576 472,576 C487.9,576 521.3,576 521.3,576 M575.3,751.3 L575.3,655.3 C575.313862,651.055109 573.620137,646.982962 570.6,644 C567.638831,640.947672 563.552355,639.247987 559.3,639.29884 L463.3,639.29884 C459.055109,639.286138 454.982962,640.979863 452,644 C448.947672,646.961169 447.247987,651.047645 447.29884,655.3 L447.29884,751.3 C447.286138,755.544891 448.979863,759.617038 452,762.6 C454.961169,765.652328 459.047645,767.352013 463.3,767.30116 L559.3,767.30116 C563.544891,767.313862 567.617038,765.620137 570.6,762.6 C573.659349,759.643612 575.360354,755.553963 575.3,751.3 M512,896 C300.2,896 128,723.9 128,512 C128,300.3 300.2,128 512,128 C723.8,128 896,300.2 896,512 C896,723.8 723.7,896 512,896 M512.1,0 C229.7,0 0,229.8 0,512 C0,794.2 229.8,1024 512.1,1024 C794.4,1024 1024,794.3 1024,512 C1024,229.7 794.4,0 512.1,0"
              />
            </svg>
          </span>
          <span class="pf-v6-c-button__text">View shortcuts</span>
        </button>
      </div>
    </div>
    <div class="pf-v6-c-code-editor__tab">
      <span class="pf-v6-c-code-editor__tab-icon">
        <i class="fas fa-code"></i>
      </span>
      <span class="pf-v6-c-code-editor__tab-text">HTML</span>
    </div>
  </div>
  <div class="pf-v6-c-code-editor__main">
    <div dir="ltr" class="pf-v6-c-code-editor__code">
      <pre class="pf-v6-c-code-editor__code-pre">
                code goes here
      </pre>
    </div>
  </div>
</div>

```

## Documentation

### Usage

| Class                                      | Applied to | Outcome                                                                                       |
| ------------------------------------------ | ---------- | --------------------------------------------------------------------------------------------- |
| `.pf-v6-c-code-editor`                     | `<div>`    | Initiates the code editor component. **Required**                                             |
| `.pf-v6-c-code-editor__header`             | `<div>`    | Initiates the code editor header used for the controls and tab elements. |
| `.pf-v6-c-code-editor__header-content`     | `<div>`    | Initiates the code editor header content used for the controls and tab elements. **Required** |
| `.pf-v6-c-code-editor__main`               | `<div>`    | Initiates the main container for a code editor e.g. Monaco **Required**                       |
| `.pf-v6-c-code-editor__code`               | `<div>`    | Initiates the container for code without a JS code editor. Comes with PatternFly styling.     |
| `.pf-v6-c-code-editor__controls`           | `<div>`    | Initiates the code editor controls.                                                           |
| `.pf-v6-c-code-editor__header-main`        | `<div>`    | Initiates the code editor header content area.                                                |
| `.pf-v6-c-code-editor__keyboard-shortcuts` | `<div>`    | Initiates the code editor header keyboard shortcuts area.                                     |
| `.pf-v6-c-code-editor__tab`                | `<div>`    | Initiates the code editor tab.                                                                |
| `.pf-v6-c-code-editor__tab-text`           | `<span>`   | Initiates the code editor tab text.                                                           |
| `.pf-v6-c-code-editor__tab-icon`           | `<span>`   | Initiates the code editor tab icon.                                                           |
| `.pf-v6-c-code-editor__upload`             | `<div>`    | Initiates the code editor upload border.                                                      |
| `.pf-v6-c-code-editor__container`             | `<div>`    | Initiates the container used inside `.pf-v6-c-code-editor` in PatternFly React. This is used in PatternFly React to prevent event propagation if upload is enabled or there is a provided empty state.                                                      |
| `.pf-m-full-height`             | `.pf-v6-c-code-editor`    | Modifies for full-height style.                                                   |
