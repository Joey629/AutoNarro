---
id: Navigation
section: components
---## Examples

### Default nav

```html isFullscreen
<div class="pf-v6-c-page" id="nav-basic-example">
  <div class="pf-v6-c-skip-to-content">
    <a
      class="pf-v6-c-button pf-m-primary"
      href="#main-content-nav-basic-example"
    >
      <span class="pf-v6-c-button__text">Skip to content</span>
    </a>
  </div>

  <header class="pf-v6-c-masthead" id="nav-basic-example-docked">
    <div class="pf-v6-c-masthead__main">
      <span class="pf-v6-c-masthead__toggle">
        <button
          class="pf-v6-c-button pf-m-hamburger pf-m-plain"
          type="button"
          aria-label="Global navigation"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              viewBox="0 0 10 10"
              class="pf-v6-c-button--hamburger-icon pf-v6-svg"
              width="1em"
              height="1em"
            >
              <path class="pf-v6-c-button--hamburger-icon--top" d="M1,1 L9,1" />
              <path
                class="pf-v6-c-button--hamburger-icon--middle"
                d="M1,5 L9,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--arrow"
                d="M1,5 L1,5 L1,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--bottom"
                d="M9,9 L1,9"
              />
            </svg>
          </span>
        </button>
      </span>
      <div class="pf-v6-c-masthead__brand">
        <a class="pf-v6-c-masthead__logo" href="#">
          <svg height="37px" viewBox="0 0 679 158">
            <title>PatternFly</title>
            <defs>
              <linearGradient
                x1="68%"
                y1="2.25860997e-13%"
                x2="32%"
                y2="100%"
                id="linearGradient-nav-basic-example-docked"
              >
                <stop stop-color="#2B9AF3" offset="0%" />
                <stop
                  stop-color="#73BCF7"
                  stop-opacity="0.502212631"
                  offset="100%"
                />
              </linearGradient>
            </defs>
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <g
                transform="translate(206.000000, 45.750000)"
                fill="var(--pf-t--global--text--color--regular)"
                fill-rule="nonzero"
              >
                <path
                  d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                />
                <path
                  d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                />
                <path
                  d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                />
                <path
                  d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                />
                <path
                  d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                />
                <path
                  d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                />
                <path
                  d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                />
                <polygon
                  points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                />
                <polygon
                  points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                />
                <path
                  d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                />
              </g>
              <g transform="translate(0.000000, 0.000000)">
                <path
                  d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                  fill="#0066CC"
                />
                <path
                  d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                  fill="url(#linearGradient-nav-basic-example-docked)"
                />
                <path
                  d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                  fill="url(#linearGradient-nav-basic-example-docked)"
                  transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                />
              </g>
            </g>
          </svg>
        </a>
      </div>
    </div>
    <div class="pf-v6-c-masthead__content">
      <div
        class="pf-v6-c-toolbar pf-m-static"
        id="nav-basic-example-docked-toolbar"
      >
        <div class="pf-v6-c-toolbar__content">
          <div class="pf-v6-c-toolbar__content-section">
            <div
              class="pf-v6-c-toolbar__group pf-m-align-end pf-m-spacer-none pf-m-spacer-md-on-md pf-m-action-group-plain"
            >
              <div
                class="pf-v6-c-toolbar__group pf-m-hidden pf-m-visible-on-lg pf-m-action-group-plain"
              >
                <div class="pf-v6-c-toolbar__item">
                  <button
                    class="pf-v6-c-menu-toggle pf-m-plain"
                    type="button"
                    aria-expanded="false"
                    aria-label="Application launcher"
                  >
                    <span class="pf-v6-c-menu-toggle__icon">
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
                          d="M149.333 56v80c0 13.255-10.745 24-24 24H24c-13.255 0-24-10.745-24-24V56c0-13.255 10.745-24 24-24h101.333c13.255 0 24 10.745 24 24zm181.334 240v-80c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24h101.333c13.256 0 24.001-10.745 24.001-24zm32-240v80c0 13.255 10.745 24 24 24H488c13.255 0 24-10.745 24-24V56c0-13.255-10.745-24-24-24H386.667c-13.255 0-24 10.745-24 24zm-32 80V56c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24h101.333c13.256 0 24.001-10.745 24.001-24zm-205.334 56H24c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24zM0 376v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H24c-13.255 0-24 10.745-24 24zm386.667-56H488c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H386.667c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24zm0 160H488c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H386.667c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24zM181.333 376v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
                <div class="pf-v6-c-toolbar__item">
                  <button
                    class="pf-v6-c-menu-toggle pf-m-settings pf-m-plain"
                    type="button"
                    aria-expanded="false"
                    aria-label="Settings"
                  >
                    <span class="pf-v6-c-menu-toggle__icon">
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
                          d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
                <div class="pf-v6-c-toolbar__item">
                  <button
                    class="pf-v6-c-menu-toggle pf-m-plain"
                    type="button"
                    aria-expanded="false"
                    aria-label="Help"
                  >
                    <span class="pf-v6-c-menu-toggle__icon">
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
                          d="M504 256c0 136.997-111.043 248-248 248S8 392.997 8 256C8 119.083 119.043 8 256 8s248 111.083 248 248zM262.655 90c-54.497 0-89.255 22.957-116.549 63.758-3.536 5.286-2.353 12.415 2.715 16.258l34.699 26.31c5.205 3.947 12.621 3.008 16.665-2.122 17.864-22.658 30.113-35.797 57.303-35.797 20.429 0 45.698 13.148 45.698 32.958 0 14.976-12.363 22.667-32.534 33.976C247.128 238.528 216 254.941 216 296v4c0 6.627 5.373 12 12 12h56c6.627 0 12-5.373 12-12v-1.333c0-28.462 83.186-29.647 83.186-106.667 0-58.002-60.165-102-116.531-102zM256 338c-25.365 0-46 20.635-46 46 0 25.364 20.635 46 46 46s46-20.636 46-46c0-25.365-20.635-46-46-46z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
              </div>

              <div class="pf-v6-c-toolbar__item pf-m-hidden-on-lg">
                <button
                  class="pf-v6-c-menu-toggle pf-m-plain"
                  type="button"
                  aria-expanded="false"
                  aria-label="Actions"
                >
                  <span class="pf-v6-c-menu-toggle__icon">
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
                        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
  <div class="pf-v6-c-page__sidebar">
    <div class="pf-v6-c-page__sidebar-main">
      <div class="pf-v6-c-page__sidebar-body">
        <nav
          class="pf-v6-c-nav"
          id="nav-basic-example-primary-nav"
          aria-label="Global"
        >
          <ul class="pf-v6-c-nav__list" role="list">
            <li class="pf-v6-c-nav__item">
              <a href="#" class="pf-v6-c-nav__link">
                <span class="pf-v6-c-nav__link-text">System panel</span>
              </a>
            </li>
            <li class="pf-v6-c-nav__item">
              <a
                href="#"
                class="pf-v6-c-nav__link pf-m-current"
                aria-current="page"
              >
                <span class="pf-v6-c-nav__link-text">Policy</span>
              </a>
            </li>
            <li class="pf-v6-c-nav__item">
              <a href="#" class="pf-v6-c-nav__link">
                <span class="pf-v6-c-nav__link-text">Authentication</span>
              </a>
            </li>
            <li class="pf-v6-c-nav__item">
              <a href="#" class="pf-v6-c-nav__link">
                <span class="pf-v6-c-nav__link-text">Network services</span>
              </a>
            </li>
            <li class="pf-v6-c-nav__item">
              <a href="#" class="pf-v6-c-nav__link">
                <span class="pf-v6-c-nav__link-text">Server</span>
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </div>
  <div class="pf-v6-c-page__main-container" tabindex="-1">
    <main
      class="pf-v6-c-page__main"
      tabindex="-1"
      id="main-content-nav-basic-example"
    >
      <section class="pf-v6-c-page__main-breadcrumb pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <nav class="pf-v6-c-breadcrumb" aria-label="breadcrumb">
            <ol class="pf-v6-c-breadcrumb__list" role="list">
              <li class="pf-v6-c-breadcrumb__item">
                <a href="#" class="pf-v6-c-breadcrumb__link">Section home</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a
                  href="#"
                  class="pf-v6-c-breadcrumb__link pf-m-current"
                  aria-current="page"
                >Section landing</a>
              </li>
            </ol>
          </nav>
        </div>
      </section>
      <section
        class="pf-v6-c-page__main-section pf-m-limit-width"
        aria-labelledby="main-title"
      >
        <div class="pf-v6-c-page__main-body">
          <h1
            class="pf-v6-c-content--h1 pf-m-page-title"
            id="main-title"
          >Main title</h1>
          <p class="pf-v6-c-content--p">This is a full page demo.</p>
        </div>
      </section>
      <section class="pf-v6-c-page__main-section pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <div class="pf-v6-l-gallery pf-m-gutter">
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</div>

```

### Grouped nav

```html isFullscreen
<div class="pf-v6-c-page" id="nav-grouped-nav-example">
  <div class="pf-v6-c-skip-to-content">
    <a
      class="pf-v6-c-button pf-m-primary"
      href="#main-content-nav-grouped-nav-example"
    >
      <span class="pf-v6-c-button__text">Skip to content</span>
    </a>
  </div>

  <header class="pf-v6-c-masthead" id="nav-grouped-nav-example-docked">
    <div class="pf-v6-c-masthead__main">
      <span class="pf-v6-c-masthead__toggle">
        <button
          class="pf-v6-c-button pf-m-hamburger pf-m-plain"
          type="button"
          aria-label="Global navigation"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              viewBox="0 0 10 10"
              class="pf-v6-c-button--hamburger-icon pf-v6-svg"
              width="1em"
              height="1em"
            >
              <path class="pf-v6-c-button--hamburger-icon--top" d="M1,1 L9,1" />
              <path
                class="pf-v6-c-button--hamburger-icon--middle"
                d="M1,5 L9,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--arrow"
                d="M1,5 L1,5 L1,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--bottom"
                d="M9,9 L1,9"
              />
            </svg>
          </span>
        </button>
      </span>
      <div class="pf-v6-c-masthead__brand">
        <a class="pf-v6-c-masthead__logo" href="#">
          <svg height="37px" viewBox="0 0 679 158">
            <title>PatternFly</title>
            <defs>
              <linearGradient
                x1="68%"
                y1="2.25860997e-13%"
                x2="32%"
                y2="100%"
                id="linearGradient-nav-grouped-nav-example-docked"
              >
                <stop stop-color="#2B9AF3" offset="0%" />
                <stop
                  stop-color="#73BCF7"
                  stop-opacity="0.502212631"
                  offset="100%"
                />
              </linearGradient>
            </defs>
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <g
                transform="translate(206.000000, 45.750000)"
                fill="var(--pf-t--global--text--color--regular)"
                fill-rule="nonzero"
              >
                <path
                  d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                />
                <path
                  d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                />
                <path
                  d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                />
                <path
                  d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                />
                <path
                  d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                />
                <path
                  d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                />
                <path
                  d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                />
                <polygon
                  points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                />
                <polygon
                  points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                />
                <path
                  d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                />
              </g>
              <g transform="translate(0.000000, 0.000000)">
                <path
                  d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                  fill="#0066CC"
                />
                <path
                  d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                  fill="url(#linearGradient-nav-grouped-nav-example-docked)"
                />
                <path
                  d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                  fill="url(#linearGradient-nav-grouped-nav-example-docked)"
                  transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                />
              </g>
            </g>
          </svg>
        </a>
      </div>
    </div>
    <div class="pf-v6-c-masthead__content">
      <div
        class="pf-v6-c-toolbar pf-m-static"
        id="nav-grouped-nav-example-docked-toolbar"
      >
        <div class="pf-v6-c-toolbar__content">
          <div class="pf-v6-c-toolbar__content-section">
            <div
              class="pf-v6-c-toolbar__group pf-m-align-end pf-m-spacer-none pf-m-spacer-md-on-md pf-m-action-group-plain"
            >
              <div
                class="pf-v6-c-toolbar__group pf-m-hidden pf-m-visible-on-lg pf-m-action-group-plain"
              >
                <div class="pf-v6-c-toolbar__item">
                  <button
                    class="pf-v6-c-menu-toggle pf-m-plain"
                    type="button"
                    aria-expanded="false"
                    aria-label="Application launcher"
                  >
                    <span class="pf-v6-c-menu-toggle__icon">
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
                          d="M149.333 56v80c0 13.255-10.745 24-24 24H24c-13.255 0-24-10.745-24-24V56c0-13.255 10.745-24 24-24h101.333c13.255 0 24 10.745 24 24zm181.334 240v-80c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24h101.333c13.256 0 24.001-10.745 24.001-24zm32-240v80c0 13.255 10.745 24 24 24H488c13.255 0 24-10.745 24-24V56c0-13.255-10.745-24-24-24H386.667c-13.255 0-24 10.745-24 24zm-32 80V56c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24h101.333c13.256 0 24.001-10.745 24.001-24zm-205.334 56H24c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24zM0 376v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H24c-13.255 0-24 10.745-24 24zm386.667-56H488c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H386.667c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24zm0 160H488c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H386.667c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24zM181.333 376v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
                <div class="pf-v6-c-toolbar__item">
                  <button
                    class="pf-v6-c-menu-toggle pf-m-settings pf-m-plain"
                    type="button"
                    aria-expanded="false"
                    aria-label="Settings"
                  >
                    <span class="pf-v6-c-menu-toggle__icon">
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
                          d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
                <div class="pf-v6-c-toolbar__item">
                  <button
                    class="pf-v6-c-menu-toggle pf-m-plain"
                    type="button"
                    aria-expanded="false"
                    aria-label="Help"
                  >
                    <span class="pf-v6-c-menu-toggle__icon">
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
                          d="M504 256c0 136.997-111.043 248-248 248S8 392.997 8 256C8 119.083 119.043 8 256 8s248 111.083 248 248zM262.655 90c-54.497 0-89.255 22.957-116.549 63.758-3.536 5.286-2.353 12.415 2.715 16.258l34.699 26.31c5.205 3.947 12.621 3.008 16.665-2.122 17.864-22.658 30.113-35.797 57.303-35.797 20.429 0 45.698 13.148 45.698 32.958 0 14.976-12.363 22.667-32.534 33.976C247.128 238.528 216 254.941 216 296v4c0 6.627 5.373 12 12 12h56c6.627 0 12-5.373 12-12v-1.333c0-28.462 83.186-29.647 83.186-106.667 0-58.002-60.165-102-116.531-102zM256 338c-25.365 0-46 20.635-46 46 0 25.364 20.635 46 46 46s46-20.636 46-46c0-25.365-20.635-46-46-46z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
              </div>

              <div class="pf-v6-c-toolbar__item pf-m-hidden-on-lg">
                <button
                  class="pf-v6-c-menu-toggle pf-m-plain"
                  type="button"
                  aria-expanded="false"
                  aria-label="Actions"
                >
                  <span class="pf-v6-c-menu-toggle__icon">
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
                        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
  <div class="pf-v6-c-page__sidebar">
    <div class="pf-v6-c-page__sidebar-main">
      <div class="pf-v6-c-page__sidebar-body">
        <nav
          class="pf-v6-c-nav"
          id="nav-grouped-nav-example-grouped-nav"
          aria-label="Global"
        >
          <section
            class="pf-v6-c-nav__section"
            aria-labelledby="grouped-title1"
          >
            <h2
              class="pf-v6-c-nav__section-title"
              id="grouped-title1"
            >System panel</h2>
            <ul class="pf-v6-c-nav__list" role="list">
              <li class="pf-v6-c-nav__item">
                <a href="#" class="pf-v6-c-nav__link">
                  <span class="pf-v6-c-nav__link-text">Overview</span>
                </a>
              </li>
              <li class="pf-v6-c-nav__item">
                <a href="#" class="pf-v6-c-nav__link">
                  <span class="pf-v6-c-nav__link-text">Resource usage</span>
                </a>
              </li>
              <li class="pf-v6-c-nav__item">
                <a
                  href="#"
                  class="pf-v6-c-nav__link pf-m-current"
                  aria-current="page"
                >
                  <span class="pf-v6-c-nav__link-text">Hypervisors</span>
                </a>
              </li>
              <li class="pf-v6-c-nav__item">
                <a href="#" class="pf-v6-c-nav__link">
                  <span class="pf-v6-c-nav__link-text">Instances</span>
                </a>
              </li>
              <li class="pf-v6-c-nav__item">
                <a href="#" class="pf-v6-c-nav__link">
                  <span class="pf-v6-c-nav__link-text">Volumes</span>
                </a>
              </li>
              <li class="pf-v6-c-nav__item">
                <a href="#" class="pf-v6-c-nav__link">
                  <span class="pf-v6-c-nav__link-text">Networks</span>
                </a>
              </li>
            </ul>
          </section>

          <section
            class="pf-v6-c-nav__section"
            aria-labelledby="grouped-title2"
          >
            <h2 class="pf-v6-c-nav__section-title" id="grouped-title2">Policy</h2>
            <ul class="pf-v6-c-nav__list" role="list">
              <li class="pf-v6-c-nav__item">
                <a href="#" class="pf-v6-c-nav__link">
                  <span class="pf-v6-c-nav__link-text">Hosts</span>
                </a>
              </li>
              <li class="pf-v6-c-nav__item">
                <a href="#" class="pf-v6-c-nav__link">
                  <span class="pf-v6-c-nav__link-text">Virtual machines</span>
                </a>
              </li>
              <li class="pf-v6-c-nav__item">
                <a href="#" class="pf-v6-c-nav__link">
                  <span class="pf-v6-c-nav__link-text">Storage</span>
                </a>
              </li>
            </ul>
          </section>
        </nav>
      </div>
    </div>
  </div>
  <div class="pf-v6-c-page__main-container" tabindex="-1">
    <main
      class="pf-v6-c-page__main"
      tabindex="-1"
      id="main-content-nav-grouped-nav-example"
    >
      <section class="pf-v6-c-page__main-breadcrumb pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <nav class="pf-v6-c-breadcrumb" aria-label="breadcrumb">
            <ol class="pf-v6-c-breadcrumb__list" role="list">
              <li class="pf-v6-c-breadcrumb__item">
                <a href="#" class="pf-v6-c-breadcrumb__link">Section home</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a
                  href="#"
                  class="pf-v6-c-breadcrumb__link pf-m-current"
                  aria-current="page"
                >Section landing</a>
              </li>
            </ol>
          </nav>
        </div>
      </section>
      <section
        class="pf-v6-c-page__main-section pf-m-limit-width"
        aria-labelledby="main-title"
      >
        <div class="pf-v6-c-page__main-body">
          <h1
            class="pf-v6-c-content--h1 pf-m-page-title"
            id="main-title"
          >Main title</h1>
          <p class="pf-v6-c-content--p">This is a full page demo.</p>
        </div>
      </section>
      <section class="pf-v6-c-page__main-section pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <div class="pf-v6-l-gallery pf-m-gutter">
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</div>

```

### Expandable nav

```html isFullscreen
<div class="pf-v6-c-page" id="nav-expandable-example">
  <div class="pf-v6-c-skip-to-content">
    <a
      class="pf-v6-c-button pf-m-primary"
      href="#main-content-nav-expandable-example"
    >
      <span class="pf-v6-c-button__text">Skip to content</span>
    </a>
  </div>

  <header class="pf-v6-c-masthead" id="nav-expandable-example-docked">
    <div class="pf-v6-c-masthead__main">
      <span class="pf-v6-c-masthead__toggle">
        <button
          class="pf-v6-c-button pf-m-hamburger pf-m-plain"
          type="button"
          aria-label="Global navigation"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              viewBox="0 0 10 10"
              class="pf-v6-c-button--hamburger-icon pf-v6-svg"
              width="1em"
              height="1em"
            >
              <path class="pf-v6-c-button--hamburger-icon--top" d="M1,1 L9,1" />
              <path
                class="pf-v6-c-button--hamburger-icon--middle"
                d="M1,5 L9,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--arrow"
                d="M1,5 L1,5 L1,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--bottom"
                d="M9,9 L1,9"
              />
            </svg>
          </span>
        </button>
      </span>
      <div class="pf-v6-c-masthead__brand">
        <a class="pf-v6-c-masthead__logo" href="#">
          <svg height="37px" viewBox="0 0 679 158">
            <title>PatternFly</title>
            <defs>
              <linearGradient
                x1="68%"
                y1="2.25860997e-13%"
                x2="32%"
                y2="100%"
                id="linearGradient-nav-expandable-example-docked"
              >
                <stop stop-color="#2B9AF3" offset="0%" />
                <stop
                  stop-color="#73BCF7"
                  stop-opacity="0.502212631"
                  offset="100%"
                />
              </linearGradient>
            </defs>
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <g
                transform="translate(206.000000, 45.750000)"
                fill="var(--pf-t--global--text--color--regular)"
                fill-rule="nonzero"
              >
                <path
                  d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                />
                <path
                  d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                />
                <path
                  d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                />
                <path
                  d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                />
                <path
                  d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                />
                <path
                  d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                />
                <path
                  d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                />
                <polygon
                  points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                />
                <polygon
                  points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                />
                <path
                  d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                />
              </g>
              <g transform="translate(0.000000, 0.000000)">
                <path
                  d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                  fill="#0066CC"
                />
                <path
                  d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                  fill="url(#linearGradient-nav-expandable-example-docked)"
                />
                <path
                  d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                  fill="url(#linearGradient-nav-expandable-example-docked)"
                  transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                />
              </g>
            </g>
          </svg>
        </a>
      </div>
    </div>
    <div class="pf-v6-c-masthead__content">
      <div
        class="pf-v6-c-toolbar pf-m-static"
        id="nav-expandable-example-docked-toolbar"
      >
        <div class="pf-v6-c-toolbar__content">
          <div class="pf-v6-c-toolbar__content-section">
            <div
              class="pf-v6-c-toolbar__group pf-m-align-end pf-m-spacer-none pf-m-spacer-md-on-md pf-m-action-group-plain"
            >
              <div
                class="pf-v6-c-toolbar__group pf-m-hidden pf-m-visible-on-lg pf-m-action-group-plain"
              >
                <div class="pf-v6-c-toolbar__item">
                  <button
                    class="pf-v6-c-menu-toggle pf-m-plain"
                    type="button"
                    aria-expanded="false"
                    aria-label="Application launcher"
                  >
                    <span class="pf-v6-c-menu-toggle__icon">
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
                          d="M149.333 56v80c0 13.255-10.745 24-24 24H24c-13.255 0-24-10.745-24-24V56c0-13.255 10.745-24 24-24h101.333c13.255 0 24 10.745 24 24zm181.334 240v-80c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24h101.333c13.256 0 24.001-10.745 24.001-24zm32-240v80c0 13.255 10.745 24 24 24H488c13.255 0 24-10.745 24-24V56c0-13.255-10.745-24-24-24H386.667c-13.255 0-24 10.745-24 24zm-32 80V56c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24h101.333c13.256 0 24.001-10.745 24.001-24zm-205.334 56H24c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24zM0 376v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H24c-13.255 0-24 10.745-24 24zm386.667-56H488c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H386.667c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24zm0 160H488c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H386.667c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24zM181.333 376v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
                <div class="pf-v6-c-toolbar__item">
                  <button
                    class="pf-v6-c-menu-toggle pf-m-settings pf-m-plain"
                    type="button"
                    aria-expanded="false"
                    aria-label="Settings"
                  >
                    <span class="pf-v6-c-menu-toggle__icon">
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
                          d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
                <div class="pf-v6-c-toolbar__item">
                  <button
                    class="pf-v6-c-menu-toggle pf-m-plain"
                    type="button"
                    aria-expanded="false"
                    aria-label="Help"
                  >
                    <span class="pf-v6-c-menu-toggle__icon">
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
                          d="M504 256c0 136.997-111.043 248-248 248S8 392.997 8 256C8 119.083 119.043 8 256 8s248 111.083 248 248zM262.655 90c-54.497 0-89.255 22.957-116.549 63.758-3.536 5.286-2.353 12.415 2.715 16.258l34.699 26.31c5.205 3.947 12.621 3.008 16.665-2.122 17.864-22.658 30.113-35.797 57.303-35.797 20.429 0 45.698 13.148 45.698 32.958 0 14.976-12.363 22.667-32.534 33.976C247.128 238.528 216 254.941 216 296v4c0 6.627 5.373 12 12 12h56c6.627 0 12-5.373 12-12v-1.333c0-28.462 83.186-29.647 83.186-106.667 0-58.002-60.165-102-116.531-102zM256 338c-25.365 0-46 20.635-46 46 0 25.364 20.635 46 46 46s46-20.636 46-46c0-25.365-20.635-46-46-46z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
              </div>

              <div class="pf-v6-c-toolbar__item pf-m-hidden-on-lg">
                <button
                  class="pf-v6-c-menu-toggle pf-m-plain"
                  type="button"
                  aria-expanded="false"
                  aria-label="Actions"
                >
                  <span class="pf-v6-c-menu-toggle__icon">
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
                        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
  <div class="pf-v6-c-page__sidebar">
    <div class="pf-v6-c-page__sidebar-main">
      <div class="pf-v6-c-page__sidebar-body">
        <nav
          class="pf-v6-c-nav"
          id="nav-expandable-example-expandable-nav"
          aria-label="Global"
        >
          <ul class="pf-v6-c-nav__list" role="list">
            <li class="pf-v6-c-nav__item pf-m-expanded">
              <button
                class="pf-v6-c-nav__link"
                aria-expanded="true"
                id="nav-expandable-example-expandable-nav-link1"
              >
                <span class="pf-v6-c-nav__link-text">System panel</span>
                <span class="pf-v6-c-nav__toggle">
                  <span class="pf-v6-c-nav__toggle-icon">
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
                        d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
                      />
                    </svg>
                  </span>
                </span>
              </button>
              <section
                class="pf-v6-c-nav__subnav"
                aria-labelledby="nav-expandable-example-expandable-nav-link1"
              >
                <ul class="pf-v6-c-nav__list" role="list">
                  <li class="pf-v6-c-nav__item">
                    <a href="#" class="pf-v6-c-nav__link">
                      <span class="pf-v6-c-nav__link-text">Overview</span>
                    </a>
                  </li>
                  <li class="pf-v6-c-nav__item">
                    <a
                      href="#"
                      class="pf-v6-c-nav__link pf-m-current"
                      aria-current="page"
                    >
                      <span class="pf-v6-c-nav__link-text">Resource usage</span>
                    </a>
                  </li>
                  <li class="pf-v6-c-nav__item">
                    <a href="#" class="pf-v6-c-nav__link">
                      <span class="pf-v6-c-nav__link-text">Hypervisors</span>
                    </a>
                  </li>
                  <li class="pf-v6-c-nav__item">
                    <a href="#" class="pf-v6-c-nav__link">
                      <span class="pf-v6-c-nav__link-text">Instances</span>
                    </a>
                  </li>
                  <li class="pf-v6-c-nav__item">
                    <a href="#" class="pf-v6-c-nav__link">
                      <span class="pf-v6-c-nav__link-text">Volumes</span>
                    </a>
                  </li>
                  <li class="pf-v6-c-nav__item">
                    <a href="#" class="pf-v6-c-nav__link">
                      <span class="pf-v6-c-nav__link-text">Networks</span>
                    </a>
                  </li>
                </ul>
              </section>
            </li>
            <li class="pf-v6-c-nav__item">
              <button
                class="pf-v6-c-nav__link"
                aria-expanded="false"
                id="nav-expandable-example-expandable-nav-link2"
              >
                <span class="pf-v6-c-nav__link-text">Policy</span>
                <span class="pf-v6-c-nav__toggle">
                  <span class="pf-v6-c-nav__toggle-icon">
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
                        d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
                      />
                    </svg>
                  </span>
                </span>
              </button>
              <section
                class="pf-v6-c-nav__subnav"
                aria-labelledby="nav-expandable-example-expandable-nav-link2"
                hidden
                inert
              >
                <ul class="pf-v6-c-nav__list" role="list">
                  <li class="pf-v6-c-nav__item">
                    <a href="#" class="pf-v6-c-nav__link">
                      <span class="pf-v6-c-nav__link-text">Subnav link 1</span>
                    </a>
                  </li>
                  <li class="pf-v6-c-nav__item">
                    <a href="#" class="pf-v6-c-nav__link">
                      <span class="pf-v6-c-nav__link-text">Subnav link 2</span>
                    </a>
                  </li>
                </ul>
              </section>
            </li>
            <li class="pf-v6-c-nav__item">
              <button
                class="pf-v6-c-nav__link"
                aria-expanded="false"
                id="nav-expandable-example-expandable-nav-link3"
              >
                <span class="pf-v6-c-nav__link-text">Authentication</span>
                <span class="pf-v6-c-nav__toggle">
                  <span class="pf-v6-c-nav__toggle-icon">
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
                        d="M18.71 5.29a.996.996 0 0 0-1.41 0l-7.29 7.29-7.3-7.29a.987.987 0 0 0-1.41-.02.987.987 0 0 0-.02 1.41l.02.02 7.65 7.65c.29.29.68.44 1.06.44s.77-.15 1.06-.44l7.65-7.65a.996.996 0 0 0 0-1.41Z"
                      />
                    </svg>
                  </span>
                </span>
              </button>
              <section
                class="pf-v6-c-nav__subnav"
                aria-labelledby="nav-expandable-example-expandable-nav-link3"
                hidden
                inert
              >
                <ul class="pf-v6-c-nav__list" role="list">
                  <li class="pf-v6-c-nav__item">
                    <a href="#" class="pf-v6-c-nav__link">
                      <span class="pf-v6-c-nav__link-text">Subnav link 1</span>
                    </a>
                  </li>
                  <li class="pf-v6-c-nav__item">
                    <a href="#" class="pf-v6-c-nav__link">
                      <span class="pf-v6-c-nav__link-text">Subnav link 2</span>
                    </a>
                  </li>
                </ul>
              </section>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </div>
  <div class="pf-v6-c-page__main-container" tabindex="-1">
    <main
      class="pf-v6-c-page__main"
      tabindex="-1"
      id="main-content-nav-expandable-example"
    >
      <section class="pf-v6-c-page__main-breadcrumb pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <nav class="pf-v6-c-breadcrumb" aria-label="breadcrumb">
            <ol class="pf-v6-c-breadcrumb__list" role="list">
              <li class="pf-v6-c-breadcrumb__item">
                <a href="#" class="pf-v6-c-breadcrumb__link">Section home</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a
                  href="#"
                  class="pf-v6-c-breadcrumb__link pf-m-current"
                  aria-current="page"
                >Section landing</a>
              </li>
            </ol>
          </nav>
        </div>
      </section>
      <section
        class="pf-v6-c-page__main-section pf-m-limit-width"
        aria-labelledby="main-title"
      >
        <div class="pf-v6-c-page__main-body">
          <h1
            class="pf-v6-c-content--h1 pf-m-page-title"
            id="main-title"
          >Main title</h1>
          <p class="pf-v6-c-content--p">This is a full page demo.</p>
        </div>
      </section>
      <section class="pf-v6-c-page__main-section pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <div class="pf-v6-l-gallery pf-m-gutter">
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</div>

```

### Horizontal nav

```html isFullscreen
<div class="pf-v6-c-page pf-m-no-sidebar" id="nav-horizontal-example">
  <div class="pf-v6-c-skip-to-content">
    <a
      class="pf-v6-c-button pf-m-primary"
      href="#main-content-nav-horizontal-example"
    >
      <span class="pf-v6-c-button__text">Skip to content</span>
    </a>
  </div>

  <header class="pf-v6-c-masthead" id="nav-horizontal-example-docked">
    <div class="pf-v6-c-masthead__main">
      <div class="pf-v6-c-masthead__brand">
        <a class="pf-v6-c-masthead__logo" href="#">
          <svg height="37px" viewBox="0 0 679 158">
            <title>PatternFly</title>
            <defs>
              <linearGradient
                x1="68%"
                y1="2.25860997e-13%"
                x2="32%"
                y2="100%"
                id="linearGradient-nav-horizontal-example-docked"
              >
                <stop stop-color="#2B9AF3" offset="0%" />
                <stop
                  stop-color="#73BCF7"
                  stop-opacity="0.502212631"
                  offset="100%"
                />
              </linearGradient>
            </defs>
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <g
                transform="translate(206.000000, 45.750000)"
                fill="var(--pf-t--global--text--color--regular)"
                fill-rule="nonzero"
              >
                <path
                  d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                />
                <path
                  d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                />
                <path
                  d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                />
                <path
                  d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                />
                <path
                  d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                />
                <path
                  d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                />
                <path
                  d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                />
                <polygon
                  points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                />
                <polygon
                  points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                />
                <path
                  d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                />
              </g>
              <g transform="translate(0.000000, 0.000000)">
                <path
                  d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                  fill="#0066CC"
                />
                <path
                  d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                  fill="url(#linearGradient-nav-horizontal-example-docked)"
                />
                <path
                  d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                  fill="url(#linearGradient-nav-horizontal-example-docked)"
                  transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                />
              </g>
            </g>
          </svg>
        </a>
      </div>
    </div>
    <div class="pf-v6-c-masthead__content">
      <div
        class="pf-v6-c-toolbar pf-m-static"
        id="nav-horizontal-example-docked-toolbar"
      >
        <div class="pf-v6-c-toolbar__content">
          <div class="pf-v6-c-toolbar__content-section">
            <div
              class="pf-v6-c-toolbar__item pf-m-overflow-container"
              style="--pf-v6-c-toolbar__item--MinWidth: 18ch;"
            >
              <nav
                class="pf-v6-c-nav pf-m-scrollable pf-m-horizontal"
                id="nav-horizontal-example-docked-horizontal-nav"
                aria-label="Global"
              >
                <div class="pf-v6-c-nav__scroll-button">
                  <button
                    class="pf-v6-c-button pf-m-plain"
                    type="button"
                    aria-label="Scroll start"
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
                          d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
                <ul class="pf-v6-c-nav__list" role="list">
                  <li class="pf-v6-c-nav__item">
                    <a href="#" class="pf-v6-c-nav__link">
                      <span class="pf-v6-c-nav__link-text">Horizontal nav item 1</span>
                    </a>
                  </li>
                  <li class="pf-v6-c-nav__item">
                    <a href="#" class="pf-v6-c-nav__link">
                      <span class="pf-v6-c-nav__link-text">Horizontal nav item 2</span>
                    </a>
                  </li>
                  <li class="pf-v6-c-nav__item">
                    <a href="#" class="pf-v6-c-nav__link">
                      <span class="pf-v6-c-nav__link-text">Horizontal nav item 3</span>
                    </a>
                  </li>
                  <li class="pf-v6-c-nav__item">
                    <a href="#" class="pf-v6-c-nav__link">
                      <span class="pf-v6-c-nav__link-text">Horizontal nav item 4</span>
                    </a>
                  </li>
                  <li class="pf-v6-c-nav__item">
                    <a
                      href="#"
                      class="pf-v6-c-nav__link pf-m-current"
                      aria-current="page"
                    >
                      <span class="pf-v6-c-nav__link-text">Horizontal nav item 5</span>
                    </a>
                  </li>
                </ul>
                <div class="pf-v6-c-nav__scroll-button">
                  <button
                    class="pf-v6-c-button pf-m-plain"
                    type="button"
                    aria-label="Scroll end"
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
                          d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
              </nav>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
  <div class="pf-v6-c-page__main-container" tabindex="-1">
    <main
      class="pf-v6-c-page__main"
      tabindex="-1"
      id="main-content-nav-horizontal-example"
    >
      <section class="pf-v6-c-page__main-breadcrumb pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <nav class="pf-v6-c-breadcrumb" aria-label="breadcrumb">
            <ol class="pf-v6-c-breadcrumb__list" role="list">
              <li class="pf-v6-c-breadcrumb__item">
                <a href="#" class="pf-v6-c-breadcrumb__link">Section home</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a
                  href="#"
                  class="pf-v6-c-breadcrumb__link pf-m-current"
                  aria-current="page"
                >Section landing</a>
              </li>
            </ol>
          </nav>
        </div>
      </section>
      <section
        class="pf-v6-c-page__main-section pf-m-limit-width"
        aria-labelledby="main-title"
      >
        <div class="pf-v6-c-page__main-body">
          <h1
            class="pf-v6-c-content--h1 pf-m-page-title"
            id="main-title"
          >Main title</h1>
          <p class="pf-v6-c-content--p">This is a full page demo.</p>
        </div>
      </section>
      <section class="pf-v6-c-page__main-section pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <div class="pf-v6-l-gallery pf-m-gutter">
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</div>

```

### Horizontal subnav

```html isFullscreen
<div class="pf-v6-c-page" id="nav-horizontal-subnav-example">
  <div class="pf-v6-c-skip-to-content">
    <a
      class="pf-v6-c-button pf-m-primary"
      href="#main-content-nav-horizontal-subnav-example"
    >
      <span class="pf-v6-c-button__text">Skip to content</span>
    </a>
  </div>

  <header class="pf-v6-c-masthead" id="nav-horizontal-subnav-example-docked">
    <div class="pf-v6-c-masthead__main">
      <span class="pf-v6-c-masthead__toggle">
        <button
          class="pf-v6-c-button pf-m-hamburger pf-m-plain"
          type="button"
          aria-label="Global navigation"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              viewBox="0 0 10 10"
              class="pf-v6-c-button--hamburger-icon pf-v6-svg"
              width="1em"
              height="1em"
            >
              <path class="pf-v6-c-button--hamburger-icon--top" d="M1,1 L9,1" />
              <path
                class="pf-v6-c-button--hamburger-icon--middle"
                d="M1,5 L9,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--arrow"
                d="M1,5 L1,5 L1,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--bottom"
                d="M9,9 L1,9"
              />
            </svg>
          </span>
        </button>
      </span>
      <div class="pf-v6-c-masthead__brand">
        <a class="pf-v6-c-masthead__logo" href="#">
          <svg height="37px" viewBox="0 0 679 158">
            <title>PatternFly</title>
            <defs>
              <linearGradient
                x1="68%"
                y1="2.25860997e-13%"
                x2="32%"
                y2="100%"
                id="linearGradient-nav-horizontal-subnav-example-docked"
              >
                <stop stop-color="#2B9AF3" offset="0%" />
                <stop
                  stop-color="#73BCF7"
                  stop-opacity="0.502212631"
                  offset="100%"
                />
              </linearGradient>
            </defs>
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <g
                transform="translate(206.000000, 45.750000)"
                fill="var(--pf-t--global--text--color--regular)"
                fill-rule="nonzero"
              >
                <path
                  d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                />
                <path
                  d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                />
                <path
                  d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                />
                <path
                  d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                />
                <path
                  d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                />
                <path
                  d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                />
                <path
                  d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                />
                <polygon
                  points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                />
                <polygon
                  points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                />
                <path
                  d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                />
              </g>
              <g transform="translate(0.000000, 0.000000)">
                <path
                  d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                  fill="#0066CC"
                />
                <path
                  d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                  fill="url(#linearGradient-nav-horizontal-subnav-example-docked)"
                />
                <path
                  d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                  fill="url(#linearGradient-nav-horizontal-subnav-example-docked)"
                  transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                />
              </g>
            </g>
          </svg>
        </a>
      </div>
    </div>
    <div class="pf-v6-c-masthead__content">
      <div
        class="pf-v6-c-toolbar pf-m-static"
        id="nav-horizontal-subnav-example-docked-toolbar"
      >
        <div class="pf-v6-c-toolbar__content">
          <div class="pf-v6-c-toolbar__content-section">
            <div
              class="pf-v6-c-toolbar__group pf-m-align-end pf-m-spacer-none pf-m-spacer-md-on-md pf-m-action-group-plain"
            >
              <div
                class="pf-v6-c-toolbar__group pf-m-hidden pf-m-visible-on-lg pf-m-action-group-plain"
              >
                <div class="pf-v6-c-toolbar__item">
                  <button
                    class="pf-v6-c-menu-toggle pf-m-plain"
                    type="button"
                    aria-expanded="false"
                    aria-label="Application launcher"
                  >
                    <span class="pf-v6-c-menu-toggle__icon">
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
                          d="M149.333 56v80c0 13.255-10.745 24-24 24H24c-13.255 0-24-10.745-24-24V56c0-13.255 10.745-24 24-24h101.333c13.255 0 24 10.745 24 24zm181.334 240v-80c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24h101.333c13.256 0 24.001-10.745 24.001-24zm32-240v80c0 13.255 10.745 24 24 24H488c13.255 0 24-10.745 24-24V56c0-13.255-10.745-24-24-24H386.667c-13.255 0-24 10.745-24 24zm-32 80V56c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24h101.333c13.256 0 24.001-10.745 24.001-24zm-205.334 56H24c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24zM0 376v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H24c-13.255 0-24 10.745-24 24zm386.667-56H488c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H386.667c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24zm0 160H488c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H386.667c-13.255 0-24 10.745-24 24v80c0 13.255 10.745 24 24 24zM181.333 376v80c0 13.255 10.745 24 24 24h101.333c13.255 0 24-10.745 24-24v-80c0-13.255-10.745-24-24-24H205.333c-13.255 0-24 10.745-24 24z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
                <div class="pf-v6-c-toolbar__item">
                  <button
                    class="pf-v6-c-menu-toggle pf-m-settings pf-m-plain"
                    type="button"
                    aria-expanded="false"
                    aria-label="Settings"
                  >
                    <span class="pf-v6-c-menu-toggle__icon">
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
                          d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
                <div class="pf-v6-c-toolbar__item">
                  <button
                    class="pf-v6-c-menu-toggle pf-m-plain"
                    type="button"
                    aria-expanded="false"
                    aria-label="Help"
                  >
                    <span class="pf-v6-c-menu-toggle__icon">
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
                          d="M504 256c0 136.997-111.043 248-248 248S8 392.997 8 256C8 119.083 119.043 8 256 8s248 111.083 248 248zM262.655 90c-54.497 0-89.255 22.957-116.549 63.758-3.536 5.286-2.353 12.415 2.715 16.258l34.699 26.31c5.205 3.947 12.621 3.008 16.665-2.122 17.864-22.658 30.113-35.797 57.303-35.797 20.429 0 45.698 13.148 45.698 32.958 0 14.976-12.363 22.667-32.534 33.976C247.128 238.528 216 254.941 216 296v4c0 6.627 5.373 12 12 12h56c6.627 0 12-5.373 12-12v-1.333c0-28.462 83.186-29.647 83.186-106.667 0-58.002-60.165-102-116.531-102zM256 338c-25.365 0-46 20.635-46 46 0 25.364 20.635 46 46 46s46-20.636 46-46c0-25.365-20.635-46-46-46z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
              </div>

              <div class="pf-v6-c-toolbar__item pf-m-hidden-on-lg">
                <button
                  class="pf-v6-c-menu-toggle pf-m-plain"
                  type="button"
                  aria-expanded="false"
                  aria-label="Actions"
                >
                  <span class="pf-v6-c-menu-toggle__icon">
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
                        d="M12.25 5c0-2.068 1.683-3.75 3.75-3.75S19.75 2.932 19.75 5 18.067 8.75 16 8.75 12.25 7.068 12.25 5ZM16 12.25c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Zm0 11c-2.067 0-3.75 1.682-3.75 3.75s1.683 3.75 3.75 3.75 3.75-1.682 3.75-3.75-1.683-3.75-3.75-3.75Z"
                      />
                    </svg>
                  </span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
  <div class="pf-v6-c-page__sidebar">
    <div class="pf-v6-c-page__sidebar-main">
      <div class="pf-v6-c-page__sidebar-body">
        <nav
          class="pf-v6-c-nav"
          id="nav-horizontal-subnav-example-primary-nav"
          aria-label="Global"
        >
          <ul class="pf-v6-c-nav__list" role="list">
            <li class="pf-v6-c-nav__item">
              <a href="#" class="pf-v6-c-nav__link">
                <span class="pf-v6-c-nav__link-text">System panel</span>
              </a>
            </li>
            <li class="pf-v6-c-nav__item">
              <a
                href="#"
                class="pf-v6-c-nav__link pf-m-current"
                aria-current="page"
              >
                <span class="pf-v6-c-nav__link-text">Policy</span>
              </a>
            </li>
            <li class="pf-v6-c-nav__item">
              <a href="#" class="pf-v6-c-nav__link">
                <span class="pf-v6-c-nav__link-text">Authentication</span>
              </a>
            </li>
            <li class="pf-v6-c-nav__item">
              <a href="#" class="pf-v6-c-nav__link">
                <span class="pf-v6-c-nav__link-text">Network services</span>
              </a>
            </li>
            <li class="pf-v6-c-nav__item">
              <a href="#" class="pf-v6-c-nav__link">
                <span class="pf-v6-c-nav__link-text">Server</span>
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </div>
  <div class="pf-v6-c-page__main-container" tabindex="-1">
    <main
      class="pf-v6-c-page__main"
      tabindex="-1"
      id="main-content-nav-horizontal-subnav-example"
    >
      <section class="pf-v6-c-page__main-subnav pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <nav
            class="pf-v6-c-nav pf-m-horizontal pf-m-subnav"
            aria-label="Local"
          >
            <ul class="pf-v6-c-nav__list" role="list">
              <li class="pf-v6-c-nav__item">
                <a
                  href="#"
                  class="pf-v6-c-nav__link pf-m-current"
                  aria-current="page"
                >
                  <span class="pf-v6-c-nav__link-text">Horizontal subnav item 1</span>
                </a>
              </li>
              <li class="pf-v6-c-nav__item">
                <a href="#" class="pf-v6-c-nav__link">
                  <span class="pf-v6-c-nav__link-text">Horizontal subnav item 2</span>
                </a>
              </li>
            </ul>
          </nav>
        </div>
      </section>
      <section class="pf-v6-c-page__main-breadcrumb pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <nav class="pf-v6-c-breadcrumb" aria-label="breadcrumb">
            <ol class="pf-v6-c-breadcrumb__list" role="list">
              <li class="pf-v6-c-breadcrumb__item">
                <a href="#" class="pf-v6-c-breadcrumb__link">Section home</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a
                  href="#"
                  class="pf-v6-c-breadcrumb__link pf-m-current"
                  aria-current="page"
                >Section landing</a>
              </li>
            </ol>
          </nav>
        </div>
      </section>
      <section
        class="pf-v6-c-page__main-section pf-m-limit-width"
        aria-labelledby="main-title"
      >
        <div class="pf-v6-c-page__main-body">
          <h1
            class="pf-v6-c-content--h1 pf-m-page-title"
            id="main-title"
          >Main title</h1>
          <p class="pf-v6-c-content--p">This is a full page demo.</p>
        </div>
      </section>
      <section class="pf-v6-c-page__main-section pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <div class="pf-v6-l-gallery pf-m-gutter">
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</div>

```

### Horizontal nav with horizontal subnav

```html isFullscreen
<div class="pf-v6-c-page pf-m-no-sidebar" id="nav-horizontal-example">
  <div class="pf-v6-c-skip-to-content">
    <a
      class="pf-v6-c-button pf-m-primary"
      href="#main-content-nav-horizontal-example"
    >
      <span class="pf-v6-c-button__text">Skip to content</span>
    </a>
  </div>

  <header
    class="pf-v6-c-masthead pf-m-display-stack pf-m-display-inline-on-lg"
    id="nav-horizontal-example-docked"
  >
    <div class="pf-v6-c-masthead__main">
      <div class="pf-v6-c-masthead__brand">
        <a class="pf-v6-c-masthead__logo" href="#">
          <svg height="37px" viewBox="0 0 679 158">
            <title>PatternFly</title>
            <defs>
              <linearGradient
                x1="68%"
                y1="2.25860997e-13%"
                x2="32%"
                y2="100%"
                id="linearGradient-nav-horizontal-example-docked"
              >
                <stop stop-color="#2B9AF3" offset="0%" />
                <stop
                  stop-color="#73BCF7"
                  stop-opacity="0.502212631"
                  offset="100%"
                />
              </linearGradient>
            </defs>
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <g
                transform="translate(206.000000, 45.750000)"
                fill="var(--pf-t--global--text--color--regular)"
                fill-rule="nonzero"
              >
                <path
                  d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                />
                <path
                  d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                />
                <path
                  d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                />
                <path
                  d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                />
                <path
                  d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                />
                <path
                  d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                />
                <path
                  d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                />
                <polygon
                  points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                />
                <polygon
                  points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                />
                <path
                  d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                />
              </g>
              <g transform="translate(0.000000, 0.000000)">
                <path
                  d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                  fill="#0066CC"
                />
                <path
                  d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                  fill="url(#linearGradient-nav-horizontal-example-docked)"
                />
                <path
                  d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                  fill="url(#linearGradient-nav-horizontal-example-docked)"
                  transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                />
              </g>
            </g>
          </svg>
        </a>
      </div>
    </div>
    <div class="pf-v6-c-masthead__content">
      <div
        class="pf-v6-c-toolbar pf-m-static"
        id="nav-horizontal-example-docked-toolbar"
      >
        <div class="pf-v6-c-toolbar__content">
          <div class="pf-v6-c-toolbar__content-section">
            <div
              class="pf-v6-c-toolbar__item pf-m-overflow-container"
              style="--pf-v6-c-toolbar__item--MinWidth: 18ch;"
            >
              <nav
                class="pf-v6-c-nav pf-m-scrollable pf-m-horizontal"
                id="nav-horizontal-example-docked-horizontal-nav"
                aria-label="Global"
              >
                <div class="pf-v6-c-nav__scroll-button">
                  <button
                    class="pf-v6-c-button pf-m-plain"
                    type="button"
                    aria-label="Scroll start"
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
                          d="m6.41 10 7.29-7.29.02-.02c.38-.4.37-1.03-.02-1.41-.4-.38-1.03-.37-1.41.02L4.64 8.95a1.49 1.49 0 0 0 0 2.12l7.65 7.65c.19.19.44.29.71.29.27 0 .52-.11.71-.29a.996.996 0 0 0 0-1.41l-7.29-7.29Z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
                <ul class="pf-v6-c-nav__list" role="list">
                  <li class="pf-v6-c-nav__item">
                    <a href="#" class="pf-v6-c-nav__link">
                      <span class="pf-v6-c-nav__link-text">Horizontal nav item 1</span>
                    </a>
                  </li>
                  <li class="pf-v6-c-nav__item">
                    <a href="#" class="pf-v6-c-nav__link">
                      <span class="pf-v6-c-nav__link-text">Horizontal nav item 2</span>
                    </a>
                  </li>
                  <li class="pf-v6-c-nav__item">
                    <a href="#" class="pf-v6-c-nav__link">
                      <span class="pf-v6-c-nav__link-text">Horizontal nav item 3</span>
                    </a>
                  </li>
                  <li class="pf-v6-c-nav__item">
                    <a href="#" class="pf-v6-c-nav__link">
                      <span class="pf-v6-c-nav__link-text">Horizontal nav item 4</span>
                    </a>
                  </li>
                  <li class="pf-v6-c-nav__item">
                    <a
                      href="#"
                      class="pf-v6-c-nav__link pf-m-current"
                      aria-current="page"
                    >
                      <span class="pf-v6-c-nav__link-text">Horizontal nav item 5</span>
                    </a>
                  </li>
                </ul>
                <div class="pf-v6-c-nav__scroll-button">
                  <button
                    class="pf-v6-c-button pf-m-plain"
                    type="button"
                    aria-label="Scroll end"
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
                          d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                        />
                      </svg>
                    </span>
                  </button>
                </div>
              </nav>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
  <div class="pf-v6-c-page__main-container" tabindex="-1">
    <main
      class="pf-v6-c-page__main"
      tabindex="-1"
      id="main-content-nav-horizontal-example"
    >
      <section class="pf-v6-c-page__main-subnav pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <nav
            class="pf-v6-c-nav pf-m-horizontal pf-m-subnav"
            aria-label="Local"
          >
            <ul class="pf-v6-c-nav__list" role="list">
              <li class="pf-v6-c-nav__item">
                <a
                  href="#"
                  class="pf-v6-c-nav__link pf-m-current"
                  aria-current="page"
                >
                  <span class="pf-v6-c-nav__link-text">Horizontal subnav item 1</span>
                </a>
              </li>
              <li class="pf-v6-c-nav__item">
                <a href="#" class="pf-v6-c-nav__link">
                  <span class="pf-v6-c-nav__link-text">Horizontal subnav item 2</span>
                </a>
              </li>
            </ul>
          </nav>
        </div>
      </section>
      <section class="pf-v6-c-page__main-breadcrumb pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <nav class="pf-v6-c-breadcrumb" aria-label="breadcrumb">
            <ol class="pf-v6-c-breadcrumb__list" role="list">
              <li class="pf-v6-c-breadcrumb__item">
                <a href="#" class="pf-v6-c-breadcrumb__link">Section home</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a
                  href="#"
                  class="pf-v6-c-breadcrumb__link pf-m-current"
                  aria-current="page"
                >Section landing</a>
              </li>
            </ol>
          </nav>
        </div>
      </section>
      <section
        class="pf-v6-c-page__main-section pf-m-limit-width"
        aria-labelledby="main-title"
      >
        <div class="pf-v6-c-page__main-body">
          <h1
            class="pf-v6-c-content--h1 pf-m-page-title"
            id="main-title"
          >Main title</h1>
          <p class="pf-v6-c-content--p">This is a full page demo.</p>
        </div>
      </section>
      <section class="pf-v6-c-page__main-section pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <div class="pf-v6-l-gallery pf-m-gutter">
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</div>

```

### Docked nav

```html isFullscreen isBeta
<div class="pf-v6-c-page pf-m-docked" id="nav-docked-example">
  <div class="pf-v6-c-skip-to-content">
    <a
      class="pf-v6-c-button pf-m-primary"
      href="#main-content-nav-docked-example"
    >
      <span class="pf-v6-c-button__text">Skip to content</span>
    </a>
  </div>
  <header class="pf-v6-c-masthead pf-m-display-inline">
    <div class="pf-v6-c-masthead__main">
      <span class="pf-v6-c-masthead__toggle">
        <button
          class="pf-v6-c-button pf-m-hamburger pf-m-plain"
          type="button"
          aria-label="Global navigation"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              viewBox="0 0 10 10"
              class="pf-v6-c-button--hamburger-icon pf-v6-svg"
              width="1em"
              height="1em"
            >
              <path class="pf-v6-c-button--hamburger-icon--top" d="M1,1 L9,1" />
              <path
                class="pf-v6-c-button--hamburger-icon--middle"
                d="M1,5 L9,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--arrow"
                d="M1,5 L1,5 L1,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--bottom"
                d="M9,9 L1,9"
              />
            </svg>
          </span>
        </button>
      </span>
      <div class="pf-v6-c-masthead__brand">
        <a class="pf-v6-c-masthead__logo" href="#">
          <svg height="37px" viewBox="0 0 679 158">
            <title>PatternFly</title>
            <defs>
              <linearGradient
                x1="68%"
                y1="2.25860997e-13%"
                x2="32%"
                y2="100%"
                id="linearGradient-"
              >
                <stop stop-color="#2B9AF3" offset="0%" />
                <stop
                  stop-color="#73BCF7"
                  stop-opacity="0.502212631"
                  offset="100%"
                />
              </linearGradient>
            </defs>
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <g
                transform="translate(206.000000, 45.750000)"
                fill="var(--pf-t--global--text--color--regular)"
                fill-rule="nonzero"
              >
                <path
                  d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                />
                <path
                  d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                />
                <path
                  d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                />
                <path
                  d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                />
                <path
                  d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                />
                <path
                  d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                />
                <path
                  d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                />
                <polygon
                  points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                />
                <polygon
                  points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                />
                <path
                  d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                />
              </g>
              <g transform="translate(0.000000, 0.000000)">
                <path
                  d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                  fill="#0066CC"
                />
                <path
                  d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                  fill="url(#linearGradient-)"
                />
                <path
                  d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                  fill="url(#linearGradient-)"
                  transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                />
              </g>
            </g>
          </svg>
        </a>
      </div>
    </div>
    <div class="pf-v6-c-masthead__content">
      <div class="pf-v6-c-toolbar pf-m-static">
        <div class="pf-v6-c-toolbar__content">
          <div class="pf-v6-c-toolbar__content-section">
            <div class="pf-v6-c-toolbar__item pf-m-align-end">
              <button
                class="pf-v6-c-button pf-m-plain"
                type="button"
                aria-label="Search"
              >
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
                      d="m30.796 29.205-8.557-8.557A11.945 11.945 0 0 0 25 13c0-6.617-5.383-12-12-12S1 6.383 1 13s5.383 12 12 12c2.904 0 5.57-1.038 7.648-2.761l8.556 8.556a1.122 1.122 0 0 0 1.592 0 1.127 1.127 0 0 0 0-1.591ZM3 13C3 7.486 7.486 3 13 3s10 4.486 10 10-4.486 10-10 10S3 18.514 3 13Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
  <div class="pf-v6-c-page__dock">
    <div class="pf-v6-c-page__dock-main">
      <header
        class="pf-v6-c-masthead pf-m-docked"
        id="nav-docked-example-masthead"
      >
        <div class="pf-v6-c-masthead__main">
          <span class="pf-v6-c-masthead__toggle">
            <button
              class="pf-v6-c-button pf-m-hamburger pf-m-plain"
              type="button"
              aria-label="Global navigation"
            >
              <span class="pf-v6-c-button__icon">
                <svg
                  viewBox="0 0 10 10"
                  class="pf-v6-c-button--hamburger-icon pf-v6-svg"
                  width="1em"
                  height="1em"
                >
                  <path
                    class="pf-v6-c-button--hamburger-icon--top"
                    d="M1,1 L9,1"
                  />
                  <path
                    class="pf-v6-c-button--hamburger-icon--middle"
                    d="M1,5 L9,5"
                  />
                  <path
                    class="pf-v6-c-button--hamburger-icon--arrow"
                    d="M1,5 L1,5 L1,5"
                  />
                  <path
                    class="pf-v6-c-button--hamburger-icon--bottom"
                    d="M9,9 L1,9"
                  />
                </svg>
              </span>
            </button>
          </span>
          <div class="pf-v6-c-masthead__brand">
            <a class="pf-v6-c-masthead__logo" href="#">
              <svg height="37px" viewBox="0 0 679 158">
                <title>PatternFly</title>
                <defs>
                  <linearGradient
                    x1="68%"
                    y1="2.25860997e-13%"
                    x2="32%"
                    y2="100%"
                    id="linearGradient-nav-docked-example-masthead"
                  >
                    <stop stop-color="#2B9AF3" offset="0%" />
                    <stop
                      stop-color="#73BCF7"
                      stop-opacity="0.502212631"
                      offset="100%"
                    />
                  </linearGradient>
                </defs>
                <g
                  stroke="none"
                  stroke-width="1"
                  fill="none"
                  fill-rule="evenodd"
                >
                  <g
                    transform="translate(206.000000, 45.750000)"
                    fill="var(--pf-t--global--text--color--regular)"
                    fill-rule="nonzero"
                  >
                    <path
                      d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                    />
                    <path
                      d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                    />
                    <path
                      d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                    />
                    <path
                      d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                    />
                    <path
                      d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                    />
                    <path
                      d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                    />
                    <path
                      d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                    />
                    <polygon
                      points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                    />
                    <polygon
                      points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                    />
                    <path
                      d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                    />
                  </g>
                  <g transform="translate(0.000000, 0.000000)">
                    <path
                      d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                      fill="#0066CC"
                    />
                    <path
                      d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                      fill="url(#linearGradient-nav-docked-example-masthead)"
                    />
                    <path
                      d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                      fill="url(#linearGradient-nav-docked-example-masthead)"
                      transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                    />
                  </g>
                </g>
              </svg>
            </a>
            <a class="pf-v6-c-masthead__logo pf-m-compact" href="#">
              <svg width="37px" height="37px" viewBox="0 0 158 158">
                <title>PatternFly</title>
                <defs>
                  <linearGradient
                    x1="68%"
                    y1="2.25860997e-13%"
                    x2="32%"
                    y2="100%"
                    id="linearGradient-1"
                  >
                    <stop stop-color="#2B9AF3" offset="0%" />
                    <stop
                      stop-color="#73BCF7"
                      stop-opacity="0.502212631"
                      offset="100%"
                    />
                  </linearGradient>
                </defs>
                <g
                  id="PF-IconLogo-color"
                  stroke="none"
                  stroke-width="1"
                  fill="none"
                  fill-rule="evenodd"
                >
                  <g id="Logo">
                    <path
                      d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                      id="Rectangle-Copy-17"
                      fill="#0066CC"
                    />
                    <path
                      d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                      id="Path-2"
                      fill="url(#linearGradient-1)"
                    />
                    <path
                      d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                      id="Path-2"
                      fill="url(#linearGradient-1)"
                      transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                    />
                  </g>
                </g>
              </svg>
            </a>
          </div>
        </div>
        <hr class="pf-v6-c-divider" />
        <div class="pf-v6-c-masthead__content">
          <div
            class="pf-v6-c-toolbar pf-m-vertical pf-m-static"
            id="nav-docked-example-masthead-toolbar"
          >
            <div class="pf-v6-c-toolbar__content">
              <div class="pf-v6-c-toolbar__content-section">
                <nav class="pf-v6-c-nav pf-m-docked" aria-label="Global">
                  <ul class="pf-v6-c-nav__list" role="list">
                    <li class="pf-v6-c-nav__item">
                      <a href="#" class="pf-v6-c-nav__link" aria-label="Cubes">
                        <span class="pf-v6-c-nav__link-icon">
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
                              d="M12.5 12h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5v7c0 .827.673 1.5 1.5 1.5Zm.5-8h6v6h-6V4ZM5.5 25h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5v7c0 .827.673 1.5 1.5 1.5Zm.5-8h6v6H6v-6Zm24 12a1 1 0 0 1-1 1H3a1 1 0 0 1 0-2h26a1 1 0 0 1 1 1ZM18 16.5v7c0 .827.673 1.5 1.5 1.5h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5Zm2 .5h6v6h-6v-6Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-nav__link-text">System panel</span>
                      </a>
                    </li>
                    <li class="pf-v6-c-nav__item">
                      <a
                        href="#"
                        class="pf-v6-c-nav__link pf-m-current"
                        aria-current="page"
                        aria-label="Folder"
                      >
                        <span class="pf-v6-c-nav__link-icon">
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
                              d="M29.5 8H17.81l-.681-3.208A1 1 0 0 0 16.15 4h-9.3a1 1 0 0 0-.979.792L5.19 8H2.5C1.673 8 1 8.673 1 9.5v17c0 .827.673 1.5 1.5 1.5h27c.827 0 1.5-.673 1.5-1.5v-17c0-.827-.673-1.5-1.5-1.5ZM29 26H3V10h3a1 1 0 0 0 .979-.792L7.66 6h7.682l.681 3.208a1 1 0 0 0 .979.792h12v16Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-nav__link-text">Policy</span>
                      </a>
                    </li>
                    <li class="pf-v6-c-nav__item">
                      <a href="#" class="pf-v6-c-nav__link" aria-label="Cloud">
                        <span class="pf-v6-c-nav__link-icon">
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
                              d="M26.996 14.228c.003-.077.004-.153.004-.228 0-4.962-4.037-9-9-9-3.899 0-7.333 2.532-8.54 6.156A6.891 6.891 0 0 0 8 11c-3.859 0-7 3.14-7 7s3.141 7 7 7h17.5c3.032 0 5.5-2.467 5.5-5.5a5.456 5.456 0 0 0-4.004-5.272ZM25.5 23H8c-2.757 0-5-2.243-5-5s2.243-5 5-5a4.97 4.97 0 0 1 1.799.34 1.003 1.003 0 0 0 1.341-.735C11.796 9.357 14.682 7 18 7c3.859 0 7 3.14 7 7 0 .311-.028.615-.067.916a1.004 1.004 0 0 0 .898 1.123 3.473 3.473 0 0 1 3.17 3.461c0 1.93-1.57 3.5-3.5 3.5Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-nav__link-text">Authentication</span>
                      </a>
                    </li>
                    <li class="pf-v6-c-nav__item">
                      <a href="#" class="pf-v6-c-nav__link" aria-label="Code">
                        <span class="pf-v6-c-nav__link-icon">
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
                              d="M9.707 9.707 3.414 16l6.293 6.293a.999.999 0 1 1-1.414 1.414l-6.646-6.646a1.501 1.501 0 0 1 0-2.121l6.646-6.646a.999.999 0 1 1 1.414 1.414Zm20.647 5.232-6.646-6.646a.999.999 0 1 0-1.414 1.414L28.587 16l-6.293 6.293a.999.999 0 1 0 1.414 1.414l6.646-6.646a1.501 1.501 0 0 0 0-2.121ZM18.121 6.022a.997.997 0 0 0-1.186.77l-3.826 18a1 1 0 1 0 1.956.416l3.826-18a1 1 0 0 0-.77-1.186Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-nav__link-text">Network services</span>
                      </a>
                    </li>
                  </ul>
                </nav>

                <div
                  class="pf-v6-c-toolbar__group pf-m-align-end pf-m-spacer-none pf-m-spacer-md-on-md pf-m-action-group-plain"
                >
                  <div class="pf-v6-c-toolbar__item">
                    <button
                      class="pf-v6-c-menu-toggle pf-m-docked pf-m-text pf-m-plain"
                      type="button"
                      aria-expanded="false"
                      aria-label="Applications"
                    >
                      <span class="pf-v6-c-menu-toggle__icon">
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
                            d="M13.75 2H3.25C2.561 2 2 2.561 2 3.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25V3.25C15 2.561 14.439 2 13.75 2ZM13 13H4V4h9v9ZM28.75 2h-10.5C17.561 2 17 2.561 17 3.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25V3.25C30 2.561 29.439 2 28.75 2ZM28 13h-9V4h9v9Zm-14.25 4H3.25C2.561 17 2 17.561 2 18.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25v-10.5c0-.689-.561-1.25-1.25-1.25ZM13 28H4v-9h9v9Zm15.75-11h-10.5c-.689 0-1.25.561-1.25 1.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25v-10.5c0-.689-.561-1.25-1.25-1.25ZM28 28h-9v-9h9v9Z"
                          />
                        </svg>
                      </span>
                      <span class="pf-v6-c-menu-toggle__text">Applications</span>
                    </button>
                  </div>
                  <div class="pf-v6-c-toolbar__item">
                    <button
                      class="pf-v6-c-button pf-m-docked pf-m-settings pf-m-plain"
                      type="button"
                      aria-label="Settings"
                    >
                      <span class="pf-v6-c-button__icon pf-m-start">
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
                            d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
                          />
                        </svg>
                      </span>
                      <span class="pf-v6-c-button__text">Settings</span>
                    </button>
                  </div>
                  <div class="pf-v6-c-toolbar__item">
                    <button
                      class="pf-v6-c-menu-toggle pf-m-docked pf-m-text pf-m-plain"
                      type="button"
                      aria-expanded="false"
                      aria-label="Help"
                    >
                      <span class="pf-v6-c-menu-toggle__icon">
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
                      <span class="pf-v6-c-menu-toggle__text">Help</span>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </header>
    </div>
  </div>
  <div class="pf-v6-c-page__main-container" tabindex="-1">
    <main
      class="pf-v6-c-page__main"
      tabindex="-1"
      id="main-content-nav-docked-example"
    >
      <section class="pf-v6-c-page__main-breadcrumb pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <nav class="pf-v6-c-breadcrumb" aria-label="breadcrumb">
            <ol class="pf-v6-c-breadcrumb__list" role="list">
              <li class="pf-v6-c-breadcrumb__item">
                <a href="#" class="pf-v6-c-breadcrumb__link">Section home</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a
                  href="#"
                  class="pf-v6-c-breadcrumb__link pf-m-current"
                  aria-current="page"
                >Section landing</a>
              </li>
            </ol>
          </nav>
        </div>
      </section>
      <section
        class="pf-v6-c-page__main-section pf-m-limit-width"
        aria-labelledby="main-title"
      >
        <div class="pf-v6-c-page__main-body">
          <h1
            class="pf-v6-c-content--h1 pf-m-page-title"
            id="main-title"
          >Main title</h1>
          <p class="pf-v6-c-content--p">This is a full page demo.</p>
        </div>
      </section>
      <section class="pf-v6-c-page__main-section pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <div class="pf-v6-l-gallery pf-m-gutter">
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</div>

```

### Docked nav - expanded on mobile

```html isFullscreen isBeta
<div class="pf-v6-c-page pf-m-docked" id="nav-docked-expanded-example">
  <div class="pf-v6-c-skip-to-content">
    <a
      class="pf-v6-c-button pf-m-primary"
      href="#main-content-nav-docked-expanded-example"
    >
      <span class="pf-v6-c-button__text">Skip to content</span>
    </a>
  </div>
  <header class="pf-v6-c-masthead pf-m-display-inline">
    <div class="pf-v6-c-masthead__main">
      <span class="pf-v6-c-masthead__toggle">
        <button
          class="pf-v6-c-button pf-m-hamburger pf-m-plain"
          type="button"
          aria-label="Global navigation"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              viewBox="0 0 10 10"
              class="pf-v6-c-button--hamburger-icon pf-v6-svg"
              width="1em"
              height="1em"
            >
              <path class="pf-v6-c-button--hamburger-icon--top" d="M1,1 L9,1" />
              <path
                class="pf-v6-c-button--hamburger-icon--middle"
                d="M1,5 L9,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--arrow"
                d="M1,5 L1,5 L1,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--bottom"
                d="M9,9 L1,9"
              />
            </svg>
          </span>
        </button>
      </span>
      <div class="pf-v6-c-masthead__brand">
        <a class="pf-v6-c-masthead__logo" href="#">
          <svg height="37px" viewBox="0 0 679 158">
            <title>PatternFly</title>
            <defs>
              <linearGradient
                x1="68%"
                y1="2.25860997e-13%"
                x2="32%"
                y2="100%"
                id="linearGradient-"
              >
                <stop stop-color="#2B9AF3" offset="0%" />
                <stop
                  stop-color="#73BCF7"
                  stop-opacity="0.502212631"
                  offset="100%"
                />
              </linearGradient>
            </defs>
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <g
                transform="translate(206.000000, 45.750000)"
                fill="var(--pf-t--global--text--color--regular)"
                fill-rule="nonzero"
              >
                <path
                  d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                />
                <path
                  d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                />
                <path
                  d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                />
                <path
                  d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                />
                <path
                  d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                />
                <path
                  d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                />
                <path
                  d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                />
                <polygon
                  points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                />
                <polygon
                  points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                />
                <path
                  d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                />
              </g>
              <g transform="translate(0.000000, 0.000000)">
                <path
                  d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                  fill="#0066CC"
                />
                <path
                  d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                  fill="url(#linearGradient-)"
                />
                <path
                  d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                  fill="url(#linearGradient-)"
                  transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                />
              </g>
            </g>
          </svg>
        </a>
      </div>
    </div>
    <div class="pf-v6-c-masthead__content">
      <div class="pf-v6-c-toolbar pf-m-static">
        <div class="pf-v6-c-toolbar__content">
          <div class="pf-v6-c-toolbar__content-section">
            <div class="pf-v6-c-toolbar__item pf-m-align-end">
              <button
                class="pf-v6-c-button pf-m-plain"
                type="button"
                aria-label="Search"
              >
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
                      d="m30.796 29.205-8.557-8.557A11.945 11.945 0 0 0 25 13c0-6.617-5.383-12-12-12S1 6.383 1 13s5.383 12 12 12c2.904 0 5.57-1.038 7.648-2.761l8.556 8.556a1.122 1.122 0 0 0 1.592 0 1.127 1.127 0 0 0 0-1.591ZM3 13C3 7.486 7.486 3 13 3s10 4.486 10 10-4.486 10-10 10S3 18.514 3 13Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
  <div class="pf-v6-c-page__dock pf-m-expanded">
    <div class="pf-v6-c-page__dock-main">
      <header
        class="pf-v6-c-masthead pf-m-docked"
        id="nav-docked-expanded-example-masthead"
      >
        <div class="pf-v6-c-masthead__main">
          <span class="pf-v6-c-masthead__toggle">
            <button
              class="pf-v6-c-button pf-m-hamburger pf-m-plain"
              type="button"
              aria-label="Global navigation"
            >
              <span class="pf-v6-c-button__icon">
                <svg
                  viewBox="0 0 10 10"
                  class="pf-v6-c-button--hamburger-icon pf-v6-svg"
                  width="1em"
                  height="1em"
                >
                  <path
                    class="pf-v6-c-button--hamburger-icon--top"
                    d="M1,1 L9,1"
                  />
                  <path
                    class="pf-v6-c-button--hamburger-icon--middle"
                    d="M1,5 L9,5"
                  />
                  <path
                    class="pf-v6-c-button--hamburger-icon--arrow"
                    d="M1,5 L1,5 L1,5"
                  />
                  <path
                    class="pf-v6-c-button--hamburger-icon--bottom"
                    d="M9,9 L1,9"
                  />
                </svg>
              </span>
            </button>
          </span>
          <div class="pf-v6-c-masthead__brand">
            <a class="pf-v6-c-masthead__logo" href="#">
              <svg height="37px" viewBox="0 0 679 158">
                <title>PatternFly</title>
                <defs>
                  <linearGradient
                    x1="68%"
                    y1="2.25860997e-13%"
                    x2="32%"
                    y2="100%"
                    id="linearGradient-nav-docked-expanded-example-masthead"
                  >
                    <stop stop-color="#2B9AF3" offset="0%" />
                    <stop
                      stop-color="#73BCF7"
                      stop-opacity="0.502212631"
                      offset="100%"
                    />
                  </linearGradient>
                </defs>
                <g
                  stroke="none"
                  stroke-width="1"
                  fill="none"
                  fill-rule="evenodd"
                >
                  <g
                    transform="translate(206.000000, 45.750000)"
                    fill="var(--pf-t--global--text--color--regular)"
                    fill-rule="nonzero"
                  >
                    <path
                      d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                    />
                    <path
                      d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                    />
                    <path
                      d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                    />
                    <path
                      d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                    />
                    <path
                      d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                    />
                    <path
                      d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                    />
                    <path
                      d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                    />
                    <polygon
                      points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                    />
                    <polygon
                      points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                    />
                    <path
                      d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                    />
                  </g>
                  <g transform="translate(0.000000, 0.000000)">
                    <path
                      d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                      fill="#0066CC"
                    />
                    <path
                      d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                      fill="url(#linearGradient-nav-docked-expanded-example-masthead)"
                    />
                    <path
                      d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                      fill="url(#linearGradient-nav-docked-expanded-example-masthead)"
                      transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                    />
                  </g>
                </g>
              </svg>
            </a>
            <a class="pf-v6-c-masthead__logo pf-m-compact" href="#">
              <svg width="37px" height="37px" viewBox="0 0 158 158">
                <title>PatternFly</title>
                <defs>
                  <linearGradient
                    x1="68%"
                    y1="2.25860997e-13%"
                    x2="32%"
                    y2="100%"
                    id="linearGradient-1"
                  >
                    <stop stop-color="#2B9AF3" offset="0%" />
                    <stop
                      stop-color="#73BCF7"
                      stop-opacity="0.502212631"
                      offset="100%"
                    />
                  </linearGradient>
                </defs>
                <g
                  id="PF-IconLogo-color"
                  stroke="none"
                  stroke-width="1"
                  fill="none"
                  fill-rule="evenodd"
                >
                  <g id="Logo">
                    <path
                      d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                      id="Rectangle-Copy-17"
                      fill="#0066CC"
                    />
                    <path
                      d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                      id="Path-2"
                      fill="url(#linearGradient-1)"
                    />
                    <path
                      d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                      id="Path-2"
                      fill="url(#linearGradient-1)"
                      transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                    />
                  </g>
                </g>
              </svg>
            </a>
          </div>
        </div>
        <hr class="pf-v6-c-divider" />
        <div class="pf-v6-c-masthead__content">
          <div
            class="pf-v6-c-toolbar pf-m-vertical pf-m-static"
            id="nav-docked-expanded-example-masthead-toolbar"
          >
            <div class="pf-v6-c-toolbar__content">
              <div class="pf-v6-c-toolbar__content-section">
                <nav class="pf-v6-c-nav pf-m-docked" aria-label="Global">
                  <ul class="pf-v6-c-nav__list" role="list">
                    <li class="pf-v6-c-nav__item">
                      <a href="#" class="pf-v6-c-nav__link" aria-label="Cubes">
                        <span class="pf-v6-c-nav__link-icon">
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
                              d="M12.5 12h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5v7c0 .827.673 1.5 1.5 1.5Zm.5-8h6v6h-6V4ZM5.5 25h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5v7c0 .827.673 1.5 1.5 1.5Zm.5-8h6v6H6v-6Zm24 12a1 1 0 0 1-1 1H3a1 1 0 0 1 0-2h26a1 1 0 0 1 1 1ZM18 16.5v7c0 .827.673 1.5 1.5 1.5h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5Zm2 .5h6v6h-6v-6Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-nav__link-text">System panel</span>
                      </a>
                    </li>
                    <li class="pf-v6-c-nav__item">
                      <a
                        href="#"
                        class="pf-v6-c-nav__link pf-m-current"
                        aria-current="page"
                        aria-label="Folder"
                      >
                        <span class="pf-v6-c-nav__link-icon">
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
                              d="M29.5 8H17.81l-.681-3.208A1 1 0 0 0 16.15 4h-9.3a1 1 0 0 0-.979.792L5.19 8H2.5C1.673 8 1 8.673 1 9.5v17c0 .827.673 1.5 1.5 1.5h27c.827 0 1.5-.673 1.5-1.5v-17c0-.827-.673-1.5-1.5-1.5ZM29 26H3V10h3a1 1 0 0 0 .979-.792L7.66 6h7.682l.681 3.208a1 1 0 0 0 .979.792h12v16Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-nav__link-text">Policy</span>
                      </a>
                    </li>
                    <li class="pf-v6-c-nav__item">
                      <a href="#" class="pf-v6-c-nav__link" aria-label="Cloud">
                        <span class="pf-v6-c-nav__link-icon">
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
                              d="M26.996 14.228c.003-.077.004-.153.004-.228 0-4.962-4.037-9-9-9-3.899 0-7.333 2.532-8.54 6.156A6.891 6.891 0 0 0 8 11c-3.859 0-7 3.14-7 7s3.141 7 7 7h17.5c3.032 0 5.5-2.467 5.5-5.5a5.456 5.456 0 0 0-4.004-5.272ZM25.5 23H8c-2.757 0-5-2.243-5-5s2.243-5 5-5a4.97 4.97 0 0 1 1.799.34 1.003 1.003 0 0 0 1.341-.735C11.796 9.357 14.682 7 18 7c3.859 0 7 3.14 7 7 0 .311-.028.615-.067.916a1.004 1.004 0 0 0 .898 1.123 3.473 3.473 0 0 1 3.17 3.461c0 1.93-1.57 3.5-3.5 3.5Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-nav__link-text">Authentication</span>
                      </a>
                    </li>
                    <li class="pf-v6-c-nav__item">
                      <a href="#" class="pf-v6-c-nav__link" aria-label="Code">
                        <span class="pf-v6-c-nav__link-icon">
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
                              d="M9.707 9.707 3.414 16l6.293 6.293a.999.999 0 1 1-1.414 1.414l-6.646-6.646a1.501 1.501 0 0 1 0-2.121l6.646-6.646a.999.999 0 1 1 1.414 1.414Zm20.647 5.232-6.646-6.646a.999.999 0 1 0-1.414 1.414L28.587 16l-6.293 6.293a.999.999 0 1 0 1.414 1.414l6.646-6.646a1.501 1.501 0 0 0 0-2.121ZM18.121 6.022a.997.997 0 0 0-1.186.77l-3.826 18a1 1 0 1 0 1.956.416l3.826-18a1 1 0 0 0-.77-1.186Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-nav__link-text">Network services</span>
                      </a>
                    </li>
                  </ul>
                </nav>

                <div
                  class="pf-v6-c-toolbar__group pf-m-align-end pf-m-spacer-none pf-m-spacer-md-on-md pf-m-action-group-plain"
                >
                  <div class="pf-v6-c-toolbar__item">
                    <button
                      class="pf-v6-c-menu-toggle pf-m-docked pf-m-text pf-m-plain"
                      type="button"
                      aria-expanded="false"
                      aria-label="Applications"
                    >
                      <span class="pf-v6-c-menu-toggle__icon">
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
                            d="M13.75 2H3.25C2.561 2 2 2.561 2 3.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25V3.25C15 2.561 14.439 2 13.75 2ZM13 13H4V4h9v9ZM28.75 2h-10.5C17.561 2 17 2.561 17 3.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25V3.25C30 2.561 29.439 2 28.75 2ZM28 13h-9V4h9v9Zm-14.25 4H3.25C2.561 17 2 17.561 2 18.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25v-10.5c0-.689-.561-1.25-1.25-1.25ZM13 28H4v-9h9v9Zm15.75-11h-10.5c-.689 0-1.25.561-1.25 1.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25v-10.5c0-.689-.561-1.25-1.25-1.25ZM28 28h-9v-9h9v9Z"
                          />
                        </svg>
                      </span>
                      <span class="pf-v6-c-menu-toggle__text">Applications</span>
                    </button>
                  </div>
                  <div class="pf-v6-c-toolbar__item">
                    <button
                      class="pf-v6-c-button pf-m-docked pf-m-settings pf-m-plain"
                      type="button"
                      aria-label="Settings"
                    >
                      <span class="pf-v6-c-button__icon pf-m-start">
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
                            d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
                          />
                        </svg>
                      </span>
                      <span class="pf-v6-c-button__text">Settings</span>
                    </button>
                  </div>
                  <div class="pf-v6-c-toolbar__item">
                    <button
                      class="pf-v6-c-menu-toggle pf-m-docked pf-m-text pf-m-plain"
                      type="button"
                      aria-expanded="false"
                      aria-label="Help"
                    >
                      <span class="pf-v6-c-menu-toggle__icon">
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
                      <span class="pf-v6-c-menu-toggle__text">Help</span>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </header>
    </div>
  </div>
  <div class="pf-v6-c-page__main-container" tabindex="-1">
    <main
      class="pf-v6-c-page__main"
      tabindex="-1"
      id="main-content-nav-docked-expanded-example"
    >
      <section class="pf-v6-c-page__main-breadcrumb pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <nav class="pf-v6-c-breadcrumb" aria-label="breadcrumb">
            <ol class="pf-v6-c-breadcrumb__list" role="list">
              <li class="pf-v6-c-breadcrumb__item">
                <a href="#" class="pf-v6-c-breadcrumb__link">Section home</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a
                  href="#"
                  class="pf-v6-c-breadcrumb__link pf-m-current"
                  aria-current="page"
                >Section landing</a>
              </li>
            </ol>
          </nav>
        </div>
      </section>
      <section
        class="pf-v6-c-page__main-section pf-m-limit-width"
        aria-labelledby="main-title"
      >
        <div class="pf-v6-c-page__main-body">
          <h1
            class="pf-v6-c-content--h1 pf-m-page-title"
            id="main-title"
          >Main title</h1>
          <p class="pf-v6-c-content--p">This is a full page demo.</p>
        </div>
      </section>
      <section class="pf-v6-c-page__main-section pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <div class="pf-v6-l-gallery pf-m-gutter">
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</div>

```

### Docked nav text expanded

```html isFullscreen isBeta
<div class="pf-v6-c-page pf-m-docked" id="nav-docked-example">
  <div class="pf-v6-c-skip-to-content">
    <a
      class="pf-v6-c-button pf-m-primary"
      href="#main-content-nav-docked-example"
    >
      <span class="pf-v6-c-button__text">Skip to content</span>
    </a>
  </div>
  <header class="pf-v6-c-masthead pf-m-display-inline">
    <div class="pf-v6-c-masthead__main">
      <span class="pf-v6-c-masthead__toggle">
        <button
          class="pf-v6-c-button pf-m-hamburger pf-m-plain"
          type="button"
          aria-label="Global navigation"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              viewBox="0 0 10 10"
              class="pf-v6-c-button--hamburger-icon pf-v6-svg"
              width="1em"
              height="1em"
            >
              <path class="pf-v6-c-button--hamburger-icon--top" d="M1,1 L9,1" />
              <path
                class="pf-v6-c-button--hamburger-icon--middle"
                d="M1,5 L9,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--arrow"
                d="M1,5 L1,5 L1,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--bottom"
                d="M9,9 L1,9"
              />
            </svg>
          </span>
        </button>
      </span>
      <div class="pf-v6-c-masthead__brand">
        <a class="pf-v6-c-masthead__logo" href="#">
          <svg height="37px" viewBox="0 0 679 158">
            <title>PatternFly</title>
            <defs>
              <linearGradient
                x1="68%"
                y1="2.25860997e-13%"
                x2="32%"
                y2="100%"
                id="linearGradient-"
              >
                <stop stop-color="#2B9AF3" offset="0%" />
                <stop
                  stop-color="#73BCF7"
                  stop-opacity="0.502212631"
                  offset="100%"
                />
              </linearGradient>
            </defs>
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <g
                transform="translate(206.000000, 45.750000)"
                fill="var(--pf-t--global--text--color--regular)"
                fill-rule="nonzero"
              >
                <path
                  d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                />
                <path
                  d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                />
                <path
                  d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                />
                <path
                  d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                />
                <path
                  d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                />
                <path
                  d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                />
                <path
                  d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                />
                <polygon
                  points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                />
                <polygon
                  points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                />
                <path
                  d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                />
              </g>
              <g transform="translate(0.000000, 0.000000)">
                <path
                  d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                  fill="#0066CC"
                />
                <path
                  d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                  fill="url(#linearGradient-)"
                />
                <path
                  d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                  fill="url(#linearGradient-)"
                  transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                />
              </g>
            </g>
          </svg>
        </a>
      </div>
    </div>
    <div class="pf-v6-c-masthead__content">
      <div class="pf-v6-c-toolbar pf-m-static">
        <div class="pf-v6-c-toolbar__content">
          <div class="pf-v6-c-toolbar__content-section">
            <div class="pf-v6-c-toolbar__item pf-m-align-end">
              <button
                class="pf-v6-c-button pf-m-plain"
                type="button"
                aria-label="Search"
              >
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
                      d="m30.796 29.205-8.557-8.557A11.945 11.945 0 0 0 25 13c0-6.617-5.383-12-12-12S1 6.383 1 13s5.383 12 12 12c2.904 0 5.57-1.038 7.648-2.761l8.556 8.556a1.122 1.122 0 0 0 1.592 0 1.127 1.127 0 0 0 0-1.591ZM3 13C3 7.486 7.486 3 13 3s10 4.486 10 10-4.486 10-10 10S3 18.514 3 13Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
  <div class="pf-v6-c-page__dock pf-m-text-expanded">
    <div class="pf-v6-c-page__dock-main">
      <header
        class="pf-v6-c-masthead pf-m-docked"
        id="nav-docked-example-masthead"
      >
        <div class="pf-v6-c-masthead__main">
          <span class="pf-v6-c-masthead__toggle">
            <button
              class="pf-v6-c-button pf-m-hamburger pf-m-plain"
              type="button"
              aria-label="Global navigation"
            >
              <span class="pf-v6-c-button__icon">
                <svg
                  viewBox="0 0 10 10"
                  class="pf-v6-c-button--hamburger-icon pf-v6-svg"
                  width="1em"
                  height="1em"
                >
                  <path
                    class="pf-v6-c-button--hamburger-icon--top"
                    d="M1,1 L9,1"
                  />
                  <path
                    class="pf-v6-c-button--hamburger-icon--middle"
                    d="M1,5 L9,5"
                  />
                  <path
                    class="pf-v6-c-button--hamburger-icon--arrow"
                    d="M1,5 L1,5 L1,5"
                  />
                  <path
                    class="pf-v6-c-button--hamburger-icon--bottom"
                    d="M9,9 L1,9"
                  />
                </svg>
              </span>
            </button>
          </span>
          <div class="pf-v6-c-masthead__brand">
            <a class="pf-v6-c-masthead__logo" href="#">
              <svg height="37px" viewBox="0 0 679 158">
                <title>PatternFly</title>
                <defs>
                  <linearGradient
                    x1="68%"
                    y1="2.25860997e-13%"
                    x2="32%"
                    y2="100%"
                    id="linearGradient-nav-docked-example-masthead"
                  >
                    <stop stop-color="#2B9AF3" offset="0%" />
                    <stop
                      stop-color="#73BCF7"
                      stop-opacity="0.502212631"
                      offset="100%"
                    />
                  </linearGradient>
                </defs>
                <g
                  stroke="none"
                  stroke-width="1"
                  fill="none"
                  fill-rule="evenodd"
                >
                  <g
                    transform="translate(206.000000, 45.750000)"
                    fill="var(--pf-t--global--text--color--regular)"
                    fill-rule="nonzero"
                  >
                    <path
                      d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                    />
                    <path
                      d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                    />
                    <path
                      d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                    />
                    <path
                      d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                    />
                    <path
                      d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                    />
                    <path
                      d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                    />
                    <path
                      d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                    />
                    <polygon
                      points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                    />
                    <polygon
                      points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                    />
                    <path
                      d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                    />
                  </g>
                  <g transform="translate(0.000000, 0.000000)">
                    <path
                      d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                      fill="#0066CC"
                    />
                    <path
                      d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                      fill="url(#linearGradient-nav-docked-example-masthead)"
                    />
                    <path
                      d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                      fill="url(#linearGradient-nav-docked-example-masthead)"
                      transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                    />
                  </g>
                </g>
              </svg>
            </a>
            <a class="pf-v6-c-masthead__logo pf-m-compact" href="#">
              <svg width="37px" height="37px" viewBox="0 0 158 158">
                <title>PatternFly</title>
                <defs>
                  <linearGradient
                    x1="68%"
                    y1="2.25860997e-13%"
                    x2="32%"
                    y2="100%"
                    id="linearGradient-1"
                  >
                    <stop stop-color="#2B9AF3" offset="0%" />
                    <stop
                      stop-color="#73BCF7"
                      stop-opacity="0.502212631"
                      offset="100%"
                    />
                  </linearGradient>
                </defs>
                <g
                  id="PF-IconLogo-color"
                  stroke="none"
                  stroke-width="1"
                  fill="none"
                  fill-rule="evenodd"
                >
                  <g id="Logo">
                    <path
                      d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                      id="Rectangle-Copy-17"
                      fill="#0066CC"
                    />
                    <path
                      d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                      id="Path-2"
                      fill="url(#linearGradient-1)"
                    />
                    <path
                      d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                      id="Path-2"
                      fill="url(#linearGradient-1)"
                      transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                    />
                  </g>
                </g>
              </svg>
            </a>
          </div>
        </div>
        <hr class="pf-v6-c-divider" />
        <div class="pf-v6-c-masthead__content">
          <div
            class="pf-v6-c-toolbar pf-m-vertical pf-m-static"
            id="nav-docked-example-masthead-toolbar"
          >
            <div class="pf-v6-c-toolbar__content">
              <div class="pf-v6-c-toolbar__content-section">
                <nav class="pf-v6-c-nav pf-m-docked" aria-label="Global">
                  <ul class="pf-v6-c-nav__list" role="list">
                    <li class="pf-v6-c-nav__item">
                      <a href="#" class="pf-v6-c-nav__link" aria-label="Cubes">
                        <span class="pf-v6-c-nav__link-icon">
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
                              d="M12.5 12h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5v7c0 .827.673 1.5 1.5 1.5Zm.5-8h6v6h-6V4ZM5.5 25h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5v7c0 .827.673 1.5 1.5 1.5Zm.5-8h6v6H6v-6Zm24 12a1 1 0 0 1-1 1H3a1 1 0 0 1 0-2h26a1 1 0 0 1 1 1ZM18 16.5v7c0 .827.673 1.5 1.5 1.5h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5Zm2 .5h6v6h-6v-6Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-nav__link-text">System panel</span>
                      </a>
                    </li>
                    <li class="pf-v6-c-nav__item">
                      <a
                        href="#"
                        class="pf-v6-c-nav__link pf-m-current"
                        aria-current="page"
                        aria-label="Folder"
                      >
                        <span class="pf-v6-c-nav__link-icon">
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
                              d="M29.5 8H17.81l-.681-3.208A1 1 0 0 0 16.15 4h-9.3a1 1 0 0 0-.979.792L5.19 8H2.5C1.673 8 1 8.673 1 9.5v17c0 .827.673 1.5 1.5 1.5h27c.827 0 1.5-.673 1.5-1.5v-17c0-.827-.673-1.5-1.5-1.5ZM29 26H3V10h3a1 1 0 0 0 .979-.792L7.66 6h7.682l.681 3.208a1 1 0 0 0 .979.792h12v16Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-nav__link-text">Policy</span>
                      </a>
                    </li>
                    <li class="pf-v6-c-nav__item">
                      <a href="#" class="pf-v6-c-nav__link" aria-label="Cloud">
                        <span class="pf-v6-c-nav__link-icon">
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
                              d="M26.996 14.228c.003-.077.004-.153.004-.228 0-4.962-4.037-9-9-9-3.899 0-7.333 2.532-8.54 6.156A6.891 6.891 0 0 0 8 11c-3.859 0-7 3.14-7 7s3.141 7 7 7h17.5c3.032 0 5.5-2.467 5.5-5.5a5.456 5.456 0 0 0-4.004-5.272ZM25.5 23H8c-2.757 0-5-2.243-5-5s2.243-5 5-5a4.97 4.97 0 0 1 1.799.34 1.003 1.003 0 0 0 1.341-.735C11.796 9.357 14.682 7 18 7c3.859 0 7 3.14 7 7 0 .311-.028.615-.067.916a1.004 1.004 0 0 0 .898 1.123 3.473 3.473 0 0 1 3.17 3.461c0 1.93-1.57 3.5-3.5 3.5Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-nav__link-text">Authentication</span>
                      </a>
                    </li>
                    <li class="pf-v6-c-nav__item">
                      <a href="#" class="pf-v6-c-nav__link" aria-label="Code">
                        <span class="pf-v6-c-nav__link-icon">
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
                              d="M9.707 9.707 3.414 16l6.293 6.293a.999.999 0 1 1-1.414 1.414l-6.646-6.646a1.501 1.501 0 0 1 0-2.121l6.646-6.646a.999.999 0 1 1 1.414 1.414Zm20.647 5.232-6.646-6.646a.999.999 0 1 0-1.414 1.414L28.587 16l-6.293 6.293a.999.999 0 1 0 1.414 1.414l6.646-6.646a1.501 1.501 0 0 0 0-2.121ZM18.121 6.022a.997.997 0 0 0-1.186.77l-3.826 18a1 1 0 1 0 1.956.416l3.826-18a1 1 0 0 0-.77-1.186Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-nav__link-text">Network services</span>
                      </a>
                    </li>
                  </ul>
                </nav>

                <div
                  class="pf-v6-c-toolbar__group pf-m-align-end pf-m-spacer-none pf-m-spacer-md-on-md pf-m-action-group-plain"
                >
                  <div class="pf-v6-c-toolbar__item">
                    <button
                      class="pf-v6-c-menu-toggle pf-m-docked pf-m-text pf-m-plain"
                      type="button"
                      aria-expanded="false"
                      aria-label="Applications"
                    >
                      <span class="pf-v6-c-menu-toggle__icon">
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
                            d="M13.75 2H3.25C2.561 2 2 2.561 2 3.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25V3.25C15 2.561 14.439 2 13.75 2ZM13 13H4V4h9v9ZM28.75 2h-10.5C17.561 2 17 2.561 17 3.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25V3.25C30 2.561 29.439 2 28.75 2ZM28 13h-9V4h9v9Zm-14.25 4H3.25C2.561 17 2 17.561 2 18.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25v-10.5c0-.689-.561-1.25-1.25-1.25ZM13 28H4v-9h9v9Zm15.75-11h-10.5c-.689 0-1.25.561-1.25 1.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25v-10.5c0-.689-.561-1.25-1.25-1.25ZM28 28h-9v-9h9v9Z"
                          />
                        </svg>
                      </span>
                      <span class="pf-v6-c-menu-toggle__text">Applications</span>
                    </button>
                  </div>
                  <div class="pf-v6-c-toolbar__item">
                    <button
                      class="pf-v6-c-button pf-m-docked pf-m-settings pf-m-plain"
                      type="button"
                      aria-label="Settings"
                    >
                      <span class="pf-v6-c-button__icon pf-m-start">
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
                            d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
                          />
                        </svg>
                      </span>
                      <span class="pf-v6-c-button__text">Settings</span>
                    </button>
                  </div>
                  <div class="pf-v6-c-toolbar__item">
                    <button
                      class="pf-v6-c-menu-toggle pf-m-docked pf-m-text pf-m-plain"
                      type="button"
                      aria-expanded="false"
                      aria-label="Help"
                    >
                      <span class="pf-v6-c-menu-toggle__icon">
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
                      <span class="pf-v6-c-menu-toggle__text">Help</span>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </header>
    </div>
  </div>
  <div class="pf-v6-c-page__main-container" tabindex="-1">
    <main
      class="pf-v6-c-page__main"
      tabindex="-1"
      id="main-content-nav-docked-example"
    >
      <section class="pf-v6-c-page__main-breadcrumb pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <nav class="pf-v6-c-breadcrumb" aria-label="breadcrumb">
            <ol class="pf-v6-c-breadcrumb__list" role="list">
              <li class="pf-v6-c-breadcrumb__item">
                <a href="#" class="pf-v6-c-breadcrumb__link">Section home</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a
                  href="#"
                  class="pf-v6-c-breadcrumb__link pf-m-current"
                  aria-current="page"
                >Section landing</a>
              </li>
            </ol>
          </nav>
        </div>
      </section>
      <section
        class="pf-v6-c-page__main-section pf-m-limit-width"
        aria-labelledby="main-title"
      >
        <div class="pf-v6-c-page__main-body">
          <h1
            class="pf-v6-c-content--h1 pf-m-page-title"
            id="main-title"
          >Main title</h1>
          <p class="pf-v6-c-content--p">This is a full page demo.</p>
        </div>
      </section>
      <section class="pf-v6-c-page__main-section pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <div class="pf-v6-l-gallery pf-m-gutter">
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</div>

```

### Docked nav text expanded - expanded on mobile

```html isFullscreen isBeta
<div class="pf-v6-c-page pf-m-docked" id="nav-docked-expanded-example">
  <div class="pf-v6-c-skip-to-content">
    <a
      class="pf-v6-c-button pf-m-primary"
      href="#main-content-nav-docked-expanded-example"
    >
      <span class="pf-v6-c-button__text">Skip to content</span>
    </a>
  </div>
  <header class="pf-v6-c-masthead pf-m-display-inline">
    <div class="pf-v6-c-masthead__main">
      <span class="pf-v6-c-masthead__toggle">
        <button
          class="pf-v6-c-button pf-m-hamburger pf-m-plain"
          type="button"
          aria-label="Global navigation"
        >
          <span class="pf-v6-c-button__icon">
            <svg
              viewBox="0 0 10 10"
              class="pf-v6-c-button--hamburger-icon pf-v6-svg"
              width="1em"
              height="1em"
            >
              <path class="pf-v6-c-button--hamburger-icon--top" d="M1,1 L9,1" />
              <path
                class="pf-v6-c-button--hamburger-icon--middle"
                d="M1,5 L9,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--arrow"
                d="M1,5 L1,5 L1,5"
              />
              <path
                class="pf-v6-c-button--hamburger-icon--bottom"
                d="M9,9 L1,9"
              />
            </svg>
          </span>
        </button>
      </span>
      <div class="pf-v6-c-masthead__brand">
        <a class="pf-v6-c-masthead__logo" href="#">
          <svg height="37px" viewBox="0 0 679 158">
            <title>PatternFly</title>
            <defs>
              <linearGradient
                x1="68%"
                y1="2.25860997e-13%"
                x2="32%"
                y2="100%"
                id="linearGradient-"
              >
                <stop stop-color="#2B9AF3" offset="0%" />
                <stop
                  stop-color="#73BCF7"
                  stop-opacity="0.502212631"
                  offset="100%"
                />
              </linearGradient>
            </defs>
            <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
              <g
                transform="translate(206.000000, 45.750000)"
                fill="var(--pf-t--global--text--color--regular)"
                fill-rule="nonzero"
              >
                <path
                  d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                />
                <path
                  d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                />
                <path
                  d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                />
                <path
                  d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                />
                <path
                  d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                />
                <path
                  d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                />
                <path
                  d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                />
                <polygon
                  points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                />
                <polygon
                  points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                />
                <path
                  d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                />
              </g>
              <g transform="translate(0.000000, 0.000000)">
                <path
                  d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                  fill="#0066CC"
                />
                <path
                  d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                  fill="url(#linearGradient-)"
                />
                <path
                  d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                  fill="url(#linearGradient-)"
                  transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                />
              </g>
            </g>
          </svg>
        </a>
      </div>
    </div>
    <div class="pf-v6-c-masthead__content">
      <div class="pf-v6-c-toolbar pf-m-static">
        <div class="pf-v6-c-toolbar__content">
          <div class="pf-v6-c-toolbar__content-section">
            <div class="pf-v6-c-toolbar__item pf-m-align-end">
              <button
                class="pf-v6-c-button pf-m-plain"
                type="button"
                aria-label="Search"
              >
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
                      d="m30.796 29.205-8.557-8.557A11.945 11.945 0 0 0 25 13c0-6.617-5.383-12-12-12S1 6.383 1 13s5.383 12 12 12c2.904 0 5.57-1.038 7.648-2.761l8.556 8.556a1.122 1.122 0 0 0 1.592 0 1.127 1.127 0 0 0 0-1.591ZM3 13C3 7.486 7.486 3 13 3s10 4.486 10 10-4.486 10-10 10S3 18.514 3 13Z"
                    />
                  </svg>
                </span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
  <div class="pf-v6-c-page__dock pf-m-text-expanded pf-m-expanded">
    <div class="pf-v6-c-page__dock-main">
      <header
        class="pf-v6-c-masthead pf-m-docked"
        id="nav-docked-expanded-example-masthead"
      >
        <div class="pf-v6-c-masthead__main">
          <span class="pf-v6-c-masthead__toggle">
            <button
              class="pf-v6-c-button pf-m-hamburger pf-m-plain"
              type="button"
              aria-label="Global navigation"
            >
              <span class="pf-v6-c-button__icon">
                <svg
                  viewBox="0 0 10 10"
                  class="pf-v6-c-button--hamburger-icon pf-v6-svg"
                  width="1em"
                  height="1em"
                >
                  <path
                    class="pf-v6-c-button--hamburger-icon--top"
                    d="M1,1 L9,1"
                  />
                  <path
                    class="pf-v6-c-button--hamburger-icon--middle"
                    d="M1,5 L9,5"
                  />
                  <path
                    class="pf-v6-c-button--hamburger-icon--arrow"
                    d="M1,5 L1,5 L1,5"
                  />
                  <path
                    class="pf-v6-c-button--hamburger-icon--bottom"
                    d="M9,9 L1,9"
                  />
                </svg>
              </span>
            </button>
          </span>
          <div class="pf-v6-c-masthead__brand">
            <a class="pf-v6-c-masthead__logo" href="#">
              <svg height="37px" viewBox="0 0 679 158">
                <title>PatternFly</title>
                <defs>
                  <linearGradient
                    x1="68%"
                    y1="2.25860997e-13%"
                    x2="32%"
                    y2="100%"
                    id="linearGradient-nav-docked-expanded-example-masthead"
                  >
                    <stop stop-color="#2B9AF3" offset="0%" />
                    <stop
                      stop-color="#73BCF7"
                      stop-opacity="0.502212631"
                      offset="100%"
                    />
                  </linearGradient>
                </defs>
                <g
                  stroke="none"
                  stroke-width="1"
                  fill="none"
                  fill-rule="evenodd"
                >
                  <g
                    transform="translate(206.000000, 45.750000)"
                    fill="var(--pf-t--global--text--color--regular)"
                    fill-rule="nonzero"
                  >
                    <path
                      d="M0,65.25 L0,2.25 L33.21,2.25 C37.35,2.25 41.025,3.135 44.235,4.905 C47.445,6.675 49.98,9.09 51.84,12.15 C53.7,15.21 54.63,18.72 54.63,22.68 C54.63,26.46 53.7,29.865 51.84,32.895 C49.98,35.925 47.43,38.31 44.19,40.05 C40.95,41.79 37.29,42.66 33.21,42.66 L15.48,42.66 L15.48,65.25 L0,65.25 Z M15.48,29.88 L31.41,29.88 C33.69,29.88 35.52,29.22 36.9,27.9 C38.28,26.58 38.97,24.87 38.97,22.77 C38.97,20.61 38.28,18.855 36.9,17.505 C35.52,16.155 33.69,15.48 31.41,15.48 L15.48,15.48 L15.48,29.88 Z"
                    />
                    <path
                      d="M77.04,66.06 C73.68,66.06 70.695,65.43 68.085,64.17 C65.475,62.91 63.435,61.17 61.965,58.95 C60.495,56.73 59.76,54.18 59.76,51.3 C59.76,46.74 61.485,43.215 64.935,40.725 C68.385,38.235 73.2,36.99 79.38,36.99 C83.1,36.99 86.7,37.44 90.18,38.34 L90.18,36 C90.18,31.26 87.15,28.89 81.09,28.89 C77.49,28.89 72.69,30.15 66.69,32.67 L61.47,21.96 C69.15,18.48 76.56,16.74 83.7,16.74 C90.3,16.74 95.43,18.315 99.09,21.465 C102.75,24.615 104.58,29.04 104.58,34.74 L104.58,65.25 L90.18,65.25 L90.18,62.37 C88.26,63.69 86.235,64.635 84.105,65.205 C81.975,65.775 79.62,66.06 77.04,66.06 Z M73.62,51.03 C73.62,52.53 74.28,53.7 75.6,54.54 C76.92,55.38 78.75,55.8 81.09,55.8 C84.69,55.8 87.72,55.05 90.18,53.55 L90.18,47.43 C87.42,46.71 84.54,46.35 81.54,46.35 C79.02,46.35 77.07,46.755 75.69,47.565 C74.31,48.375 73.62,49.53 73.62,51.03 Z"
                    />
                    <path
                      d="M137.25,65.88 C125.73,65.88 119.97,60.84 119.97,50.76 L119.97,29.79 L110.34,29.79 L110.34,17.64 L119.97,17.64 L119.97,5.4 L134.55,2.25 L134.55,17.64 L147.87,17.64 L147.87,29.79 L134.55,29.79 L134.55,47.88 C134.55,49.98 135.015,51.465 135.945,52.335 C136.875,53.205 138.51,53.64 140.85,53.64 C143.01,53.64 145.2,53.31 147.42,52.65 L147.42,64.44 C146.1,64.86 144.42,65.205 142.38,65.475 C140.34,65.745 138.63,65.88 137.25,65.88 Z"
                    />
                    <path
                      d="M177.57,65.88 C166.05,65.88 160.29,60.84 160.29,50.76 L160.29,29.79 L150.66,29.79 L150.66,17.64 L160.29,17.64 L160.29,5.4 L174.87,2.25 L174.87,17.64 L188.19,17.64 L188.19,29.79 L174.87,29.79 L174.87,47.88 C174.87,49.98 175.335,51.465 176.265,52.335 C177.195,53.205 178.83,53.64 181.17,53.64 C183.33,53.64 185.52,53.31 187.74,52.65 L187.74,64.44 C186.42,64.86 184.74,65.205 182.7,65.475 C180.66,65.745 178.95,65.88 177.57,65.88 Z"
                    />
                    <path
                      d="M217.62,66.15 C212.76,66.15 208.365,65.055 204.435,62.865 C200.505,60.675 197.4,57.72 195.12,54 C192.84,50.28 191.7,46.11 191.7,41.49 C191.7,36.87 192.795,32.7 194.985,28.98 C197.175,25.26 200.16,22.305 203.94,20.115 C207.72,17.925 211.92,16.83 216.54,16.83 C221.22,16.83 225.36,17.955 228.96,20.205 C232.56,22.455 235.395,25.53 237.465,29.43 C239.535,33.33 240.57,37.8 240.57,42.84 L240.57,46.44 L206.64,46.44 C207.6,48.66 209.1,50.475 211.14,51.885 C213.18,53.295 215.58,54 218.34,54 C222.42,54 225.6,52.8 227.88,50.4 L237.51,58.95 C234.51,61.47 231.435,63.3 228.285,64.44 C225.135,65.58 221.58,66.15 217.62,66.15 Z M206.37,36.27 L226.26,36.27 C225.48,33.99 224.205,32.16 222.435,30.78 C220.665,29.4 218.61,28.71 216.27,28.71 C213.87,28.71 211.8,29.37 210.06,30.69 C208.32,32.01 207.09,33.87 206.37,36.27 Z"
                    />
                    <path
                      d="M247.41,65.25 L247.41,17.64 L261.99,17.64 L261.99,22.41 C265.23,18.51 269.4,16.56 274.5,16.56 C277.08,16.62 278.91,17.01 279.99,17.73 L279.99,30.42 C277.95,29.46 275.64,28.98 273.06,28.98 C270.78,28.98 268.665,29.505 266.715,30.555 C264.765,31.605 263.19,33.09 261.99,35.01 L261.99,65.25 L247.41,65.25 Z"
                    />
                    <path
                      d="M286.29,65.25 L286.29,17.64 L300.87,17.64 L300.87,20.88 C304.47,18.12 308.73,16.74 313.65,16.74 C317.37,16.74 320.655,17.55 323.505,19.17 C326.355,20.79 328.59,23.04 330.21,25.92 C331.83,28.8 332.64,32.13 332.64,35.91 L332.64,65.25 L318.06,65.25 L318.06,37.89 C318.06,35.25 317.28,33.15 315.72,31.59 C314.16,30.03 312.06,29.25 309.42,29.25 C305.76,29.25 302.91,30.51 300.87,33.03 L300.87,65.25 L286.29,65.25 Z"
                    />
                    <polygon
                      points="342 65.25 342 2.25 392.04 2.25 392.04 15.66 357.48 15.66 357.48 27.45 380.52 27.45 380.52 40.41 357.48 40.41 357.48 65.25"
                    />
                    <polygon
                      points="399.96 65.25 399.96 2.25 414.54 0 414.54 65.25"
                    />
                    <path
                      d="M429.21,84.69 C428.07,84.69 426.96,84.645 425.88,84.555 C424.8,84.465 423.9,84.33 423.18,84.15 L423.18,71.73 C424.38,71.97 425.88,72.09 427.68,72.09 C432.36,72.09 435.51,70.05 437.13,65.97 L437.13,65.88 L418.86,17.64 L434.97,17.64 L445.5,47.61 L457.74,17.64 L473.49,17.64 L452.16,67.68 C450.42,71.82 448.5,75.135 446.4,77.625 C444.3,80.115 441.87,81.915 439.11,83.025 C436.35,84.135 433.05,84.69 429.21,84.69 Z"
                    />
                  </g>
                  <g transform="translate(0.000000, 0.000000)">
                    <path
                      d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                      fill="#0066CC"
                    />
                    <path
                      d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                      fill="url(#linearGradient-nav-docked-expanded-example-masthead)"
                    />
                    <path
                      d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                      fill="url(#linearGradient-nav-docked-expanded-example-masthead)"
                      transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                    />
                  </g>
                </g>
              </svg>
            </a>
            <a class="pf-v6-c-masthead__logo pf-m-compact" href="#">
              <svg width="37px" height="37px" viewBox="0 0 158 158">
                <title>PatternFly</title>
                <defs>
                  <linearGradient
                    x1="68%"
                    y1="2.25860997e-13%"
                    x2="32%"
                    y2="100%"
                    id="linearGradient-1"
                  >
                    <stop stop-color="#2B9AF3" offset="0%" />
                    <stop
                      stop-color="#73BCF7"
                      stop-opacity="0.502212631"
                      offset="100%"
                    />
                  </linearGradient>
                </defs>
                <g
                  id="PF-IconLogo-color"
                  stroke="none"
                  stroke-width="1"
                  fill="none"
                  fill-rule="evenodd"
                >
                  <g id="Logo">
                    <path
                      d="M61.826087,0 L158,0 L158,96.173913 L147.695652,96.173913 C100.271201,96.173913 61.826087,57.7287992 61.826087,10.3043478 L61.826087,0 L61.826087,0 Z"
                      id="Rectangle-Copy-17"
                      fill="#0066CC"
                    />
                    <path
                      d="M158,3.43478261 L65.2608696,158 L138,158 C149.045695,158 158,149.045695 158,138 L158,3.43478261 L158,3.43478261 Z"
                      id="Path-2"
                      fill="url(#linearGradient-1)"
                    />
                    <path
                      d="M123.652174,-30.9130435 L30.9130435,123.652174 L103.652174,123.652174 C114.697869,123.652174 123.652174,114.697869 123.652174,103.652174 L123.652174,-30.9130435 L123.652174,-30.9130435 Z"
                      id="Path-2"
                      fill="url(#linearGradient-1)"
                      transform="translate(77.282609, 46.369565) scale(1, -1) rotate(90.000000) translate(-77.282609, -46.369565) "
                    />
                  </g>
                </g>
              </svg>
            </a>
          </div>
        </div>
        <hr class="pf-v6-c-divider" />
        <div class="pf-v6-c-masthead__content">
          <div
            class="pf-v6-c-toolbar pf-m-vertical pf-m-static"
            id="nav-docked-expanded-example-masthead-toolbar"
          >
            <div class="pf-v6-c-toolbar__content">
              <div class="pf-v6-c-toolbar__content-section">
                <nav class="pf-v6-c-nav pf-m-docked" aria-label="Global">
                  <ul class="pf-v6-c-nav__list" role="list">
                    <li class="pf-v6-c-nav__item">
                      <a href="#" class="pf-v6-c-nav__link" aria-label="Cubes">
                        <span class="pf-v6-c-nav__link-icon">
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
                              d="M12.5 12h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5v7c0 .827.673 1.5 1.5 1.5Zm.5-8h6v6h-6V4ZM5.5 25h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5v7c0 .827.673 1.5 1.5 1.5Zm.5-8h6v6H6v-6Zm24 12a1 1 0 0 1-1 1H3a1 1 0 0 1 0-2h26a1 1 0 0 1 1 1ZM18 16.5v7c0 .827.673 1.5 1.5 1.5h7c.827 0 1.5-.673 1.5-1.5v-7c0-.827-.673-1.5-1.5-1.5h-7c-.827 0-1.5.673-1.5 1.5Zm2 .5h6v6h-6v-6Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-nav__link-text">System panel</span>
                      </a>
                    </li>
                    <li class="pf-v6-c-nav__item">
                      <a
                        href="#"
                        class="pf-v6-c-nav__link pf-m-current"
                        aria-current="page"
                        aria-label="Folder"
                      >
                        <span class="pf-v6-c-nav__link-icon">
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
                              d="M29.5 8H17.81l-.681-3.208A1 1 0 0 0 16.15 4h-9.3a1 1 0 0 0-.979.792L5.19 8H2.5C1.673 8 1 8.673 1 9.5v17c0 .827.673 1.5 1.5 1.5h27c.827 0 1.5-.673 1.5-1.5v-17c0-.827-.673-1.5-1.5-1.5ZM29 26H3V10h3a1 1 0 0 0 .979-.792L7.66 6h7.682l.681 3.208a1 1 0 0 0 .979.792h12v16Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-nav__link-text">Policy</span>
                      </a>
                    </li>
                    <li class="pf-v6-c-nav__item">
                      <a href="#" class="pf-v6-c-nav__link" aria-label="Cloud">
                        <span class="pf-v6-c-nav__link-icon">
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
                              d="M26.996 14.228c.003-.077.004-.153.004-.228 0-4.962-4.037-9-9-9-3.899 0-7.333 2.532-8.54 6.156A6.891 6.891 0 0 0 8 11c-3.859 0-7 3.14-7 7s3.141 7 7 7h17.5c3.032 0 5.5-2.467 5.5-5.5a5.456 5.456 0 0 0-4.004-5.272ZM25.5 23H8c-2.757 0-5-2.243-5-5s2.243-5 5-5a4.97 4.97 0 0 1 1.799.34 1.003 1.003 0 0 0 1.341-.735C11.796 9.357 14.682 7 18 7c3.859 0 7 3.14 7 7 0 .311-.028.615-.067.916a1.004 1.004 0 0 0 .898 1.123 3.473 3.473 0 0 1 3.17 3.461c0 1.93-1.57 3.5-3.5 3.5Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-nav__link-text">Authentication</span>
                      </a>
                    </li>
                    <li class="pf-v6-c-nav__item">
                      <a href="#" class="pf-v6-c-nav__link" aria-label="Code">
                        <span class="pf-v6-c-nav__link-icon">
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
                              d="M9.707 9.707 3.414 16l6.293 6.293a.999.999 0 1 1-1.414 1.414l-6.646-6.646a1.501 1.501 0 0 1 0-2.121l6.646-6.646a.999.999 0 1 1 1.414 1.414Zm20.647 5.232-6.646-6.646a.999.999 0 1 0-1.414 1.414L28.587 16l-6.293 6.293a.999.999 0 1 0 1.414 1.414l6.646-6.646a1.501 1.501 0 0 0 0-2.121ZM18.121 6.022a.997.997 0 0 0-1.186.77l-3.826 18a1 1 0 1 0 1.956.416l3.826-18a1 1 0 0 0-.77-1.186Z"
                            />
                          </svg>
                        </span>
                        <span class="pf-v6-c-nav__link-text">Network services</span>
                      </a>
                    </li>
                  </ul>
                </nav>

                <div
                  class="pf-v6-c-toolbar__group pf-m-align-end pf-m-spacer-none pf-m-spacer-md-on-md pf-m-action-group-plain"
                >
                  <div class="pf-v6-c-toolbar__item">
                    <button
                      class="pf-v6-c-menu-toggle pf-m-docked pf-m-text pf-m-plain"
                      type="button"
                      aria-expanded="false"
                      aria-label="Applications"
                    >
                      <span class="pf-v6-c-menu-toggle__icon">
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
                            d="M13.75 2H3.25C2.561 2 2 2.561 2 3.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25V3.25C15 2.561 14.439 2 13.75 2ZM13 13H4V4h9v9ZM28.75 2h-10.5C17.561 2 17 2.561 17 3.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25V3.25C30 2.561 29.439 2 28.75 2ZM28 13h-9V4h9v9Zm-14.25 4H3.25C2.561 17 2 17.561 2 18.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25v-10.5c0-.689-.561-1.25-1.25-1.25ZM13 28H4v-9h9v9Zm15.75-11h-10.5c-.689 0-1.25.561-1.25 1.25v10.5c0 .689.561 1.25 1.25 1.25h10.5c.689 0 1.25-.561 1.25-1.25v-10.5c0-.689-.561-1.25-1.25-1.25ZM28 28h-9v-9h9v9Z"
                          />
                        </svg>
                      </span>
                      <span class="pf-v6-c-menu-toggle__text">Applications</span>
                    </button>
                  </div>
                  <div class="pf-v6-c-toolbar__item">
                    <button
                      class="pf-v6-c-button pf-m-docked pf-m-settings pf-m-plain"
                      type="button"
                      aria-label="Settings"
                    >
                      <span class="pf-v6-c-button__icon pf-m-start">
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
                            d="M30.168 12.894a.5.5 0 0 0-.488-.394h-2.732a11.512 11.512 0 0 0-.729-1.769l1.931-1.93a.5.5 0 0 0 .066-.625 14.693 14.693 0 0 0-4.393-4.392.498.498 0 0 0-.624.067l-1.93 1.93a11.512 11.512 0 0 0-1.769-.729V2.319a.5.5 0 0 0-.395-.489 14.81 14.81 0 0 0-6.211 0 .5.5 0 0 0-.395.489v2.733c-.614.196-1.207.439-1.769.729L8.8 3.851a.498.498 0 0 0-.624-.067 14.714 14.714 0 0 0-4.393 4.392.5.5 0 0 0 .066.625l1.931 1.93a11.512 11.512 0 0 0-.729 1.769H2.319a.5.5 0 0 0-.488.394 14.652 14.652 0 0 0 0 6.212.5.5 0 0 0 .488.394h2.732c.196.615.44 1.207.729 1.769l-1.931 1.93a.5.5 0 0 0-.066.625 14.673 14.673 0 0 0 4.393 4.392.498.498 0 0 0 .624-.067l1.93-1.93c.562.289 1.154.533 1.769.729v2.733a.5.5 0 0 0 .395.489 14.686 14.686 0 0 0 6.21 0 .5.5 0 0 0 .395-.489v-2.733a11.454 11.454 0 0 0 1.769-.729l1.93 1.93a.5.5 0 0 0 .624.067 14.714 14.714 0 0 0 4.393-4.392.5.5 0 0 0-.066-.625l-1.931-1.93c.289-.562.533-1.154.729-1.769h2.732a.5.5 0 0 0 .488-.394 14.652 14.652 0 0 0 0-6.212ZM16 21.25c-2.895 0-5.25-2.355-5.25-5.25s2.355-5.25 5.25-5.25 5.25 2.355 5.25 5.25-2.355 5.25-5.25 5.25Z"
                          />
                        </svg>
                      </span>
                      <span class="pf-v6-c-button__text">Settings</span>
                    </button>
                  </div>
                  <div class="pf-v6-c-toolbar__item">
                    <button
                      class="pf-v6-c-menu-toggle pf-m-docked pf-m-text pf-m-plain"
                      type="button"
                      aria-expanded="false"
                      aria-label="Help"
                    >
                      <span class="pf-v6-c-menu-toggle__icon">
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
                      <span class="pf-v6-c-menu-toggle__text">Help</span>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </header>
    </div>
  </div>
  <div class="pf-v6-c-page__main-container" tabindex="-1">
    <main
      class="pf-v6-c-page__main"
      tabindex="-1"
      id="main-content-nav-docked-expanded-example"
    >
      <section class="pf-v6-c-page__main-breadcrumb pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <nav class="pf-v6-c-breadcrumb" aria-label="breadcrumb">
            <ol class="pf-v6-c-breadcrumb__list" role="list">
              <li class="pf-v6-c-breadcrumb__item">
                <a href="#" class="pf-v6-c-breadcrumb__link">Section home</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a href="#" class="pf-v6-c-breadcrumb__link">Section title</a>
              </li>
              <li class="pf-v6-c-breadcrumb__item">
                <span class="pf-v6-c-breadcrumb__item-divider">
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
                      d="M14.35 8.94 6.71 1.29l-.02-.02c-.4-.38-1.03-.37-1.41.02-.38.4-.37 1.03.02 1.41l7.29 7.29-7.29 7.29a1.003 1.003 0 0 0 1.42 1.42l7.65-7.65c.59-.59.59-1.54 0-2.12Z"
                    />
                  </svg>
                </span>

                <a
                  href="#"
                  class="pf-v6-c-breadcrumb__link pf-m-current"
                  aria-current="page"
                >Section landing</a>
              </li>
            </ol>
          </nav>
        </div>
      </section>
      <section
        class="pf-v6-c-page__main-section pf-m-limit-width"
        aria-labelledby="main-title"
      >
        <div class="pf-v6-c-page__main-body">
          <h1
            class="pf-v6-c-content--h1 pf-m-page-title"
            id="main-title"
          >Main title</h1>
          <p class="pf-v6-c-content--p">This is a full page demo.</p>
        </div>
      </section>
      <section class="pf-v6-c-page__main-section pf-m-limit-width">
        <div class="pf-v6-c-page__main-body">
          <div class="pf-v6-l-gallery pf-m-gutter">
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
            <div class="pf-v6-c-card">
              <div class="pf-v6-c-card__body">This is a card</div>
            </div>
          </div>
        </div>
      </section>
    </main>
  </div>
</div>

```
